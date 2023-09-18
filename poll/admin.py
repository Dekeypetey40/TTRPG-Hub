from django.contrib import admin
from poll.models import PollOption, Poll

# Register your models here.

admin.site.register(PollOption)
admin.site.register(Poll)

