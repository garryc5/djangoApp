from django.db import models
from django.urls import reverse

class Wish(models.Model):
    wishs = models.CharField(max_length=150)
    def __str__(self):
        return self.wishs
   