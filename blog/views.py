from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Tags

# Create your views here.
class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3
    posts = Post.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()

class TagList(ListView):
    model = Tags
    template_name = "index.html"
    tags = Tag.objects.all()
    
class PostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked=False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            }
        )