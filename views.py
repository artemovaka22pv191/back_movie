from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':

        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def raitingStar_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        star = RaitingStar.objects.all()
        serializer = RaitingStarSerializer(star, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RaitingStarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def raitingStar_detail(request, pk):
    try:
        star = RaitingStar.objects.get(pk=pk)
    except RaitingStar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RaitingStarSerializer(star)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RaitingStarSerializer(star, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        star.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def aut(request):
    try:
        user = User.objects.get(username=request.data['username'])
        if (user.password == request.data['password']):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(request.data['password'], status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail(request, pk):
    try:
        reviews = Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewsSerializer(reviews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewsSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def raiting_list(request):
    if request.method == 'GET':
        raiting = Raiting.objects.all()
        serializer = RaitingSerializer(raiting, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RaitingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def raiting_detail(request, pk):
    try:
        raiting = Raiting.objects.get(pk=pk)
    except Raiting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RaitingSerializer(raiting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RaitingSerializer(raiting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        raiting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
