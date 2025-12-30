from django.shortcuts import render, get_object_or_404, reverse
from taggit.models import Tag
from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add liked status for each post if user is authenticated
        if self.request.user.is_authenticated:
            liked_posts = set(
                Post.objects.filter(likes=self.request.user).values_list('id', flat=True)
            )
            context['liked_posts'] = liked_posts
        else:
            context['liked_posts'] = set()
        return context

# Ability to filter blog posts by tag


class TagFilter(View):
    """The view users see when they click on a tag button"""

    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tags=tag)
        
        # Add liked status for each post if user is authenticated
        if request.user.is_authenticated:
            liked_posts = set(
                Post.objects.filter(likes=request.user).values_list('id', flat=True)
            )
        else:
            liked_posts = set()
        
        context = {
            'tag': tag,
            'posts': posts,
            'liked_posts': liked_posts,
        }
        return render(request, 'tag_filter.html', context)


class PostDetail(View):
    """The view for looking at a blog post"""

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        liked = False
        if request.user.is_authenticated:
            liked = post.likes.filter(id=request.user.id).exists()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")

        liked = False
        if request.user.is_authenticated:
            liked = post.likes.filter(id=request.user.id).exists()

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, "You have posted your comment!")
            commented = True
            comment_form = CommentForm()  # reset after success
        else:
            commented = False  # don't claim success if invalid

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": commented,
                "liked": liked,
                "comment_form": comment_form,
            },
        )



class PostLike(View):
    """Adding or removing likes on a post"""

    def post(self, request, slug):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Authentication required'}, status=401)
            return HttpResponseRedirect(reverse('account_login'))

        post = get_object_or_404(Post, slug=slug)

        # Check if user has already liked the post
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        # If AJAX request, return JSON response
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'liked': liked,
                'likes_count': post.number_of_likes()
            })

        # Otherwise, redirect back to the page the user came from (fallback)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))


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
