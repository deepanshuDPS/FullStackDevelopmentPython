from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)