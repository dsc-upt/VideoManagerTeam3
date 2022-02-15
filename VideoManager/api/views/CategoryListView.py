from django.http import JsonResponse, HttpResponse
from rest_framework import generics, status
from api.serializers.CategorySerializer import CategorySerializer
from api.models.CategoryModel import CategoryModel
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def category_list(request, pk):
    if request.method == "GET":
        category = CategoryModel.objects.filter(pk=pk)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if CategoryModel.objects.filter(name=request.data['name']).exists():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        category = CategoryModel.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category = CategoryModel.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)