from django.urls import path
from poll.views import HomeView, PollView

app_name = "poll"

urlpatterns = [
    path("poll/", HomeView.as_view(), name="list"),
    path("poll/<int:poll_id>/", PollView.as_view(), name="poll"),
]
