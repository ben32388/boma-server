from django.contrib import admin

from .models import Folder
# admin.site.register(Post)
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'user_id']
    
