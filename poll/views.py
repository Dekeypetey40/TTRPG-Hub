from django.shortcuts import render
from django.views import View

from poll.models import Poll, PollOption, Vote
# Create your views here.

# Written so that if one were to make more
# polls in the future one could make a polls
# homepage and have the user select the poll
# they want to vote on.

class HomeView(View):

    def get(self, request):
        polls = Poll.objects.all()
        return render(
            request,
            template_name="poll_home.html",
            context={
                "polls": polls,
            }
        )

class PollView(View):
    
    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="poll.html",
            context={
                "poll": poll,
            }
        )
        
    def post(self, request, poll_id):
        requestData = request.POST
        
        option_id = requestData.get('option_id')
        
        poll = Poll.objects.get(id=poll_id)
        option = PollOption.objects.get(id=option_id)
        Vote.objects.create(
            poll=poll,
            option=option,
        )
        
        return render(
            request,
            template_name="poll.html",
            context={
                "poll": poll,
                "success_message": "Thanks for voting",
            }
        )