from django.db import models
from .CategoryModel import CategoryModel

class VideoModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
