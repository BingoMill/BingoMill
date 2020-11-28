from django.db import models

# Create your models here.
class Bingo(models.Model):
    # title = models.CharField(max_length=20)
    # password =  models.CharField(max_length=100)
    # username = models.CharField(max_length=30)
    # words = models.ArrayField(models.CharField(max_length=30, blank=True),size=37)
    # wordSize = models.IntegerField()

    def __str__(self):
        return self.question_text