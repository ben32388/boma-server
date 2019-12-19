from django.contrib import admin

from .models import Page

@admin.register(Page)
class FolderAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'url', 'tags', 'folder', 'user_id']
    
