from django.shortcuts import render
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
# Create your views here.

@api_view(['POST'])
def get_sound_in_level1(request):
    sound_id = request.data.get('sound_id', None)
    
    if sound_id:
        try:
            Target_sound = Level_1_const.objects.get(id=sound_id)
            serializer = Leve_1_serializer(Target_sound, context={'request': request})
            json = {
                "status": "success",
                "data":  serializer.data
                
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Sound with the specified id does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter sound_id."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_sound_in_level2(request):
    sound_id = request.data.get('sound_id', None)
    
    if sound_id:
        try:
            Target_sound = Level_2_v_d.objects.get(id=sound_id)
            serializer = Leve_2_serializer(Target_sound, context={'request': request})
            json = {
                "status": "success",
                "data":  serializer.data
                
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Sound with the specified id does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter sound_id."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_sound_in_level3(request):
    sound_id = request.data.get('Sentence_id', None)
    
    if sound_id:
        try:
            Target_sound = Level_3_sent.objects.get(id=sound_id)
            serializer = Leve_3_serializer(Target_sound, context={'request': request})
            json = {
                "status": "success",
                "data":  serializer.data
                
            }
            return Response(json)
        except ObjectDoesNotExist:
            return Response({"message": "Sentence with the specified id does not exist."}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"message": "You should enter Sentence_id."}, status=status.HTTP_400_BAD_REQUEST)


class get_all_ReadingTest(viewsets.ModelViewSet):
    queryset = ReadingTest.objects.all()
    serializer_class = ReadingTest_serializer 
    
    def list(self, request, *args, **kwargs):
        response = super(get_all_ReadingTest, self).list(request, *args, **kwargs)
        
        formatted_response = {
            "status": "success",
            "data":  response.data
            
        }
        
        return Response(formatted_response) 