from django.db import models
from django.contrib.postgres.fields import ArrayField


class Bingo(models.Model):
    title = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    words = models.CharField(max_length=2000)
    words_size = models.IntegerField(default=0)

    def __str__(self):
        return self.title
