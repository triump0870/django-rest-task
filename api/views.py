from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from imdb.models import Movie
from api.serializers import MovieSerializer
# Create your views here.

class MovieListView(generics.ListCreateAPIView):
    """
    List all the Movies, or create a new Movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request):
        serializer =self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    # def create(self, request, *args, **kwrags):
    #     genre_data = request.DATA['genres']
    #     serializer = self.get_serializer(data=genres, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         headers = self.get_success_header(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GenreListView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = GenreSerializer
