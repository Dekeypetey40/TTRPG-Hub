from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib import messages

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
        poll = Poll.objects.get(id=poll_id)
        if request.user.is_authenticated:
            requestData = request.POST
            option_id = requestData.get('option_id')

            option = PollOption.objects.get(id=option_id)
            if not Vote.objects.filter(poll=poll, user=request.user).exists():
                Vote.objects.create(
                    poll=poll,
                    option=option,
                    user=request.user
                )
                poll_results = []
                for option in poll.options.all():
                    voteCount = Vote.objects.filter(poll=poll,
                                                    option=option).count()
                    poll_results.append([option.name, voteCount])

                return render(
                    request,
                    template_name="poll.html",
                    context={
                        "poll": poll,
                        "success_message": "Thanks for voting",
                        "poll_results": poll_results,
                    }
                )
            else:
                poll_results = []
                for option in poll.options.all():
                    voteCount = Vote.objects.filter(poll=poll,
                                                    option=option).count()
                    poll_results.append([option.name, voteCount])
                return render(
                    request,
                    template_name="poll.html",
                    context={
                        "poll": poll,
                        "failure_message": "You may only vote once",
                        "poll_results": poll_results,
                    }
                )
        else:
            messages.warning(self.request, "You must be logged in to vote")
            return redirect(reverse('poll:poll', kwargs={'poll_id': poll.id}))
