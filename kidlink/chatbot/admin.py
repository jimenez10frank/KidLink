from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'tokens_used', 'cost', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'message', 'response']
    readonly_fields = ['created_at']
    
    def has_delete_permission(self, request, obj=None):
        return True