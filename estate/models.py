from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,null=True)
    occupant_count = models.IntegerField(null=True)
    
    