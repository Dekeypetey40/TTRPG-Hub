from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class PollOption(models.Model):
    """
    Model a poll option
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Poll(models.Model):
    """
    Model for a poll
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    options = models.ManyToManyField(
        PollOption, related_name='related_polls', blank=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    """
    Need a vote model so that when a poll uses the same option as
    another that the votes get tallied properly.
    """
    poll = models.ForeignKey(Poll,
                             on_delete=models.SET_NULL,
                             related_name="votes",
                             null=True,
                             blank=True)
    option = models.ForeignKey(PollOption,
                               on_delete=models.SET_NULL,
                               related_name="votes",
                               null=True,
                               blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             related_name="votes",
                             null=True,
                             blank=True)

    def __str__(self):
        return f"{self.poll.name} - {self.option.name}"
