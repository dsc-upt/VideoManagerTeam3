from django.contrib import admin
from api.models.VideoModel import VideoModel
from api.models.CategoryModel import CategoryModel

admin.site.register(VideoModel)
admin.site.register(CategoryModel)