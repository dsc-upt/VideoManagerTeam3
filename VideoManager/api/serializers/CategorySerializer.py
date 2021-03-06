from rest_framework import serializers
from api.models.CategoryModel import CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"