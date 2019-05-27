from django.db import models
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)