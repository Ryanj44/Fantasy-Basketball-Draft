from django.db import models

# Create your models here.
class Player(models.Model):
    ranking = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length = 45)
    position = models.CharField(max_length = 45)
    team = models.CharField(max_length = 45)
    points = models.DecimalField(max_digits=4, decimal_places=1)
    rebounds = models.DecimalField(max_digits=4, decimal_places=1)
    assists = models.DecimalField(max_digits=4, decimal_places=1)
    steals = models.DecimalField(max_digits=4, decimal_places=1)
    blocks = models.DecimalField(max_digits=4, decimal_places=1)
    turnovers = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
    name = models.CharField(max_length = 45)
    pick = models.IntegerField()
    players = models.ManyToManyField(Player, related_name = "teams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

