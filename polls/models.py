import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # optional first positional argument to a Field to designate a human-readable name
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    '''
    It’s important to add __str__() methods to your models, not only for your own convenience 
    when dealing with the interactive prompt, but also because objects’ representations are 
    used throughout Django’s automatically-generated admin.

    https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.__str__
    '''
    def __str__(self):
        return question_text


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return choise_text
