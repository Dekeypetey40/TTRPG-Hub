from django.shortcuts import render, get_object_or_404, reverse
from taggit.models import Tag
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from django import http
from .forms import CommentForm

# View for the homepage with blog posts


class PostList(ListView):
    """Post List for the home page"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3
    posts = Post.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()

# Ability to filter blog posts by tag


class TagFilter(View):
    """The view users see when they click on a tag button"""

    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tags=tag)
        context = {
            'tag': tag,
            'posts': posts,
        }
        return render(request, 'tag_filter.html', context)


class PostDetail(View):
    """The view for looking at a blog post"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'You have posted your comment!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """Adding or removing likes on a post"""

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class EditComment(UpdateView):
    """Edit user comment on the front end"""
    model = Comment
    form_class = CommentForm
    template_name = "edit_comment.html"

    def get_success_url_edit(self):
        post = self.object.post
        post_slug = post.slug
        messages.success(self.request,
                         'You have successfully edited your comment!')
        return reverse('post_detail', kwargs={'slug': post_slug})


class DeleteComment(DeleteView):
    """View for user to delete comment in front end"""
    model = Comment
    template_name = "delete_comment.html"

    def get_success_url_edit(self):
        post = self.object.post
        post_slug = post.slug
        messages.success(self.request,
                         'You have successfully deleted your comment!')
        return reverse('post_detail', kwargs={'slug': post_slug})
