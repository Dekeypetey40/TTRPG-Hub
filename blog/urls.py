from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('tag/<slug:slug>/', views.TagFilter.as_view(), name='tagged'),
    path('edit_comment/<int:pk>/', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<int:pk>/', views.DeleteComment.as_view(),
         name='delete_comment'),
]
