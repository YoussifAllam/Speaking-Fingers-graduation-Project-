from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from django.http import HttpResponse
from . models import *
from rest_framework import viewsets, status , generics , permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.decorators import api_view, permission_classes,parser_classes
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class FavoriteVideoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetFavoriteVideoSerializer
    
    def get_queryset(self):
        return FavoriteVideos.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        response = super(FavoriteVideoListCreateView, self).list(request, *args, **kwargs)
        # Now modify the response data as desired
        formatted_response = {
            "status": "success",
            "data": response.data  # Use the data from the original response
        }
        return Response(formatted_response)

class VideoListView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        response = super(VideoListView, self).list(request, *args, **kwargs)

        if request.user.is_authenticated:
            # Get a list of video IDs that the current user has favorited
            favorite_video_ids = set(FavoriteVideos.objects.filter(
                user=request.user
            ).values_list('video_id', flat=True))

            # Enhance each video data with 'is_fav' field
            for video_data in response.data:
                video_data['is_fav'] = video_data['id'] in favorite_video_ids
        else:
            # If user is not authenticated, mark all videos as not favorited
            for video_data in response.data:
                video_data['is_fav'] = False

        formatted_response = {
            "status": "success",
            "data": {
                "videos": response.data
            }
        }

        return Response(formatted_response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_video_details(request):
    # Use request.query_params instead of request.data for GET requests
    video_title = request.GET.get('video_title', None)
    
    if video_title:
        try:
            targetvideo = Video.objects.get(title=video_title)
            serializer = VideoSerializer(targetvideo, context={'request': request})
            json = {
                "status": "success",
                "data": {
                    "video": serializer.data
                }
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Video with the specified title does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter video_title."}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def favorite_video(request):
    serializer = FavoriteVideoSerializer(data=request.data)
    if serializer.is_valid():
        # Retrieve the video by title
        video_title = serializer.validated_data['video_title']
        if not video_title : return Response({'message': 'You must enter video_title.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            video = Video.objects.get(title=video_title)
            # video.update(is_Fav = True)
        except Video.DoesNotExist:
            return Response({'message': 'Video not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the video is already favorited by the user
        already_favorited = FavoriteVideos.objects.filter(user=request.user, video=video).exists()
        if already_favorited:
            return Response({'message': 'Video already favorited.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the FavoriteVideos instance
        FavoriteVideos.objects.create(user=request.user, video=video)
        return Response({'message': 'Video favorited successfully.'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_favorite_video(request):
    video_title = request.data.get('video_title')
    if not video_title:
        return Response({'error': 'Video title is required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Find the video by title. Consider the case sensitivity and uniqueness of titles.
    try:
        video = Video.objects.get(title=video_title)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Remove the video from the user's favorites.
    favorite_video_exists = FavoriteVideos.objects.filter(user=request.user, video=video).exists()
    if not favorite_video_exists:
        # If it does not exist, return a custom message
        return Response({'error': 'Favorite video not found in user favorite videos'}, status=status.HTTP_404_NOT_FOUND)
    
    # Since the favorite video exists, proceed with deletion
    FavoriteVideos.objects.filter(user=request.user, video=video).delete()
    return Response({'message': 'Video removed from favorites.'}, status=status.HTTP_204_NO_CONTENT)

