from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raiting
        fields = '__all__'


class RaitingStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaitingStar
        fields = '__all__'
