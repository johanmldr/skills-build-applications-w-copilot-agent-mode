from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
