from rest_framework import serializers
from django.db import IntegrityError
from rest_framework.response import Response
import re
from django.contrib.auth.password_validation import validate_password
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = '__all__'

class FavoriteVideoSerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(max_length=255)
    class Meta:
        model = FavoriteVideos
        fields = ['video_title']
        

class GetFavoriteVideoSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    class Meta:
        model = FavoriteVideos
        fields = ['added_on' , 'user' , 'video']