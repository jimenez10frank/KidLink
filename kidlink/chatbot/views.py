from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
import json
from openai import OpenAI
import os
from django.contrib.auth.decorators import login_required
from functools import wraps
from time import time

# Simple rate limiter (stores last request time per user)
_rate_limit_cache = {}

def rate_limit(max_requests=10, window=60):
    """Rate limiter: max_requests per window seconds"""
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            user_id = request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
            now = time()
            
            if user_id not in _rate_limit_cache:
                _rate_limit_cache[user_id] = []
            
            # Remove old requests outside the window
            _rate_limit_cache[user_id] = [t for t in _rate_limit_cache[user_id] if now - t < window]
            
            if len(_rate_limit_cache[user_id]) >= max_requests:
                return JsonResponse({
                    'error': f'Rate limit exceeded. Maximum {max_requests} requests per {window} seconds.'
                }, status=429)
            
            _rate_limit_cache[user_id].append(now)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required(login_url='admin_login')
def chatbot_view(request):
    """Render the chatbot Page."""
    return render(request, 'chatbot/chatbot.html')

@login_required(login_url='admin_login')
@require_http_methods(["POST"])
@rate_limit(max_requests=10, window=60)  # 10 requests per minute
def chat_api(request):
    """Handle chat messages via AJAX."""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        # Validate input
        if not user_message:
            return JsonResponse({'error': 'Message cannot be empty.'}, status=400)
        
        if len(user_message) > 500:
            return JsonResponse({'error': 'Message too long. Maximum 500 characters.'}, status=400)
        
        # Check for API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return JsonResponse({'error': 'OpenAI API key not configured.'}, status=500)
        
        # Check for API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return JsonResponse({'error': 'OpenAI API key not configured.'}, status=500)
        
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        # Enhanced system prompt with strict guidelines
        system_prompt = """You are an AI assistant for KidLink, a youth management system. Your purpose is to help administrators manage:

1. Youth records (names, dates of birth, gender, status, registration dates)
2. Activities (programs, events, youth participation tracking)
3. Institutes (schools, colleges, training centers)
4. Youth-Institute relationships
5. Youth-Activity relationships

STRICT RULES:
- ONLY answer questions about KidLink and youth management
- DO NOT write code, provide programming tutorials, or technical implementations
- DO NOT answer questions about unrelated topics (politics, weather, math, science, etc.)
- If asked about something unrelated, politely redirect: "I can only help with KidLink youth management. How can I assist you with managing youth, activities, or institutes?"
- Provide clear, concise answers about the system's features
- Use examples from youth management context when explaining concepts
- Be professional and helpful but stay focused on the system"""

        # Call OpenAI API with new syntax
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=250,
            temperature=0.5,  # Lower temperature for more focused responses
        )
        
        # Access response data AFTER the API call is complete
        ai_response = response.choices[0].message.content
        
        # Extract usage information from response
        total_tokens = response.usage.total_tokens
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        
        # Calculate cost (GPT-3.5-turbo pricing: $0.0015 per 1K input tokens, $0.002 per 1K output tokens)
        input_cost = (prompt_tokens / 1000) * 0.0015
        output_cost = (completion_tokens / 1000) * 0.002
        total_cost = input_cost + output_cost
        
        # Print to console for debugging
        print(f"\n=== OpenAI API Usage ===")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Completion tokens: {completion_tokens}")
        print(f"Total tokens: {total_tokens}")
        print(f"Cost: ${total_cost:.6f}")
        print("========================\n")
        
        # Optional: Add content filtering
        # Block responses that might be too generic or off-topic
        blocked_keywords = [
            'here is the code',
            'write code',
            'copy this',
            'here is how to',
        ]
        
        # If response contains blocked patterns and is off-topic, give a redirect message
        user_lower = user_message.lower()
        if any(keyword in ai_response.lower()[:100] for keyword in blocked_keywords):
            if not any(term in user_lower for term in ['youth', 'activity', 'institute', 'kidlink', 'manage', 'add', 'create', 'delete', 'edit']):
                ai_response = "I can only help you with KidLink youth management tasks. Please ask about managing youth records, activities, institutes, or system operations."

        # Save to database if user is authenticated
        if request.user.is_authenticated:
            from .models import ChatMessage
            ChatMessage.objects.create(
                message=user_message,
                response=ai_response,
                user=request.user,
                tokens_used=total_tokens,
                cost=total_cost
            )
        
        return JsonResponse({'response': ai_response})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)