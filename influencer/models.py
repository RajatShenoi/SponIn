from django.db import models

class Influencer(models.Model):
    category = models.CharField(max_length=100)
    niche = models.CharField(max_length=100)
    reach = models.IntegerField()