from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'updated_on', 'created_on', 'status', 'get_tags']
    
    
    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
