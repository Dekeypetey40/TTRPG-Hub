from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Post, Comment

# Create your views here.
class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3