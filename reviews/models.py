from django.db import models


# Create your models here.
class Review(models.Model):
    fullname = models.CharField(max_length=100)
    review_text = models.TextField()
    ratings = models.IntegerField()
