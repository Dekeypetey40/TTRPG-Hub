from django.urls import path
from . import views

app_name = "poll"

urlpatterns = [
    path("poll/<int:poll_id>/", views.PollView.as_view(), name="poll"),
]