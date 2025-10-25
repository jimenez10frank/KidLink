from django.contrib import admin
from .models import ChatMessage
# Register your models here.

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'response', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'message', 'response']
    readonly_fields = ['created_at']
    
    def has_delete_permission(self, request, obj=None):
        return True