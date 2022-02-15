from rest_framework import serializers
from api.models.VideoModel import VideoModel


class VideoSerializer(serializers.Serializer):
    class Meta:
        model = VideoModel
        fields = '__all__'