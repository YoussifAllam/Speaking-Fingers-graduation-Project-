from .models import User # , Video, FavoriteVideos
from rest_framework import serializers
from django.db import IntegrityError
from rest_framework.response import Response
import re
from django.contrib.auth.password_validation import validate_password
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = '__all__'

# class FavoriteVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FavoriteVideos
#         fields = ['video']

class SingUpSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'email_verified', 'profile_picture',]
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True},
                        'username': {'read_only': True},
                        }

    def validate_email(self, value):
        # Check if email is already registered
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")

        return value

    def validate_password(self, value):
        # Check for strong password
        if not re.search(r'\d', value) or not re.search('[A-Z]', value):
            raise serializers.ValidationError("Password should contain at least 1 number and 1 uppercase letter.")

        validate_password(value)
        return value

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']

        # Generate a unique username if the provided name already exists as a username
       
        base_username = re.sub(r'\s+', '_', name).lower()

        while True:
            random_number = random.randint(1000, 9999)
            unique_username = f"{base_username}_{random_number}"
            try:
                User.objects.get(username=unique_username)
            except User.DoesNotExist:
                name = unique_username
                break

        user = User.objects.create_user(
            name,
            email,
            password
        )
        user.name = validated_data['name']
        user.save()
        
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username','name' ,'email','profile_picture','phone_number') 
        
        
