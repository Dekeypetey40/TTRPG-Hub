from django.db import models

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