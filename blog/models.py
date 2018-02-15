from django.db import models
from django.utils import timezone

# Create your models here.
class Propaganda(models.Model):
    slogan = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.slogan


class Post(models.Model):
    title = models.CharField(max_length=140, blank=False, null=False)
    content = models.TextField()
    summary = models.TextField(max_length=500)
    tips = models.TextField(max_length=280, blank=False, null=False)
    created_date = models.DateTimeField()
    last_edited = models.DateTimeField()

    def __str__(self):
        return self.title
