from django.shortcuts import render
from django.views import View

from poll.models import Poll
# Create your views here.

# Written so that if one were to make more
# polls in the future one could make a polls
# homepage and have the user select the poll
# they want to vote on.
class PollView(View):
    
    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="poll/poll-html",
            context={
                "poll": poll,
            }
        )
