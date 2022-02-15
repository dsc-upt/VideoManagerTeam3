from rest_framework import generics
from api.serializers.VideoSerializer import VideoSerializer
from api.models.VideoModel import VideoModel
from rest_framework.response import Response

class ListVideosView(generics.ListCreateAPIView):
    queryset = VideoModel.objects.all()
    serializer_class = VideoSerializer