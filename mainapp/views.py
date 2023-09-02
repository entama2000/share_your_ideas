from mainapp.models import Ideas
from mainapp.serializers import IdeasSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IdeaList(APIView):
    def get(self, request, format=None):
        ideas = Ideas.objects.all()
        serializer = IdeasSerializer(ideas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdeasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IdeaDetail(APIView):
    def get_object(self, pk):
        try:
            return Ideas.objects.get(pk=pk)
        except Ideas.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idea = self.get_object(pk)
        serializer = IdeasSerializer(idea)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idea = self.get_object(pk)
        serializer = IdeasSerializer(idea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idea = self.get_object(pk)
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
