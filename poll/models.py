from django.db import models
from django.utils import timezone
# Create your models here.

class PollOption(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name



class Poll(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    choices = models.ManyToManyField(
        PollOption, related_name='related_polls', blank=True)
    
    def __str__(self):
        return self.name
    
        """
        Need a vote model so that when a poll uses the same option as
        another that the votes get tallied properly.
        """
class Vote(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    option = models.ForeignKey(
        PollOption, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return f"{self.poll.name} - {self.option.name}"
