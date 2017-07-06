from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models, migrations
import datetime                
from django.utils.timezone import localtime, now
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.


#Question Model
class Computer_Science_Quiz_Beginners(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)
    start_count = models.SmallIntegerField(default=0)
    max_counter = models.SmallIntegerField()
    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Computer Science Quiz Beginners'


class Computer_Science_Quiz_Intermediate(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)
    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Computer Science Quiz Intermediate'



class Computer_Science_Quiz_Advance(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)
    def __str__(self):
        return self.Question



    class Meta:
        verbose_name_plural = 'Computer Science Quiz Advance'



class Networking_Quiz_Beginners(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Networking Quiz Beginners'

class Networking_Quiz_Intermediate(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Networking Quiz Intermediate'


class Networking_Quiz_Advance(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Networking Quiz Advance'


class Linux_Quiz_Beginners(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Linux Quiz Beginners' 




class Linux_Quiz_Intermediate(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Linux Quiz Intermediate'





class Linux_Quiz_Advance(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Linux Quiz Advance'





class Electronic_Principal_Quiz(models.Model):
    Question = models.CharField(blank=True, max_length=400)
    choice1 = models.CharField(blank=True, max_length=400)
    choice2 = models.CharField(blank=True, max_length=400)
    choice3 = models.CharField(blank=True, max_length=400)
    choice4 = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = 'Electronic Principal Quiz'


# Check for correct answer
class Correct(models.Model):
    answer = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name_plural = 'Correct'


class Stored_Answer(models.Model):
    answer = models.CharField(max_length=400,blank=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name_plural = 'Stored Answer'


class ajax(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)