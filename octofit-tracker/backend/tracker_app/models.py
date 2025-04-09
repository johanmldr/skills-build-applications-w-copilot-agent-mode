from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Team(models.Model):
    id = models.CharField(max_length=24, primary_key=True, default='')
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)

class Activity(models.Model):
    id = models.CharField(max_length=24, primary_key=True, default='')
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    user_email = models.EmailField()
    score = models.IntegerField()

class Workout(models.Model):
    user_email = models.EmailField()
    description = models.TextField()
    date = models.DateField()