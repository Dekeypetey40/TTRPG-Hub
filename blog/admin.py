from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin 

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'created_on', 'get_tags']
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
    
    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
