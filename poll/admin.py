from django.contrib import admin
from poll.models import PollOption, Poll, Vote

# Register your models here.

admin.site.register(PollOption)
admin.site.register(Poll)
admin.site.register(Vote)
