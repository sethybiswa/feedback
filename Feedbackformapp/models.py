from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.CharField(max_length=100)

