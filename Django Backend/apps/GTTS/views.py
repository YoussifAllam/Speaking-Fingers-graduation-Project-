from rest_framework.views import APIView
from rest_framework.response import Response
import eng_to_ipa as ipa
from rest_framework import status
import os
from gtts import gTTS
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from io import BytesIO  # Import BytesIO to handle byte streams
import uuid

def get_uuid():
    name = str(uuid.uuid4()) + '.mp3'
    return name

class TextToSpeechAPI(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get('text', None)
        language = request.data.get('language', 'ar')
        # print('=========' , language)
        if language != 'ar' and language != 'en':
            return Response({"error": "You can enter 'ar' or 'en' in language parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not text or not language:
            return Response({"error": "text and language parameters is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Convert text to speech
        speech = gTTS(text=text, slow=False , lang = language)
        
        # Use BytesIO to handle the speech data
        mp3_fp = BytesIO()
        speech.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        file_name = get_uuid()
        file_path = default_storage.save(file_name, ContentFile(mp3_fp.read()))

        # Build the full URL. Note: 'request' is used to dynamically get the server's URL
        if request.is_secure():
            protocol = 'https://'
        else:
            protocol = 'http://'
        
        host = request.get_host()
        file_url = protocol + host + default_storage.url(file_path)

        return Response({
                'Status:': 'Success',
                'URL': file_url
            }, status=status.HTTP_201_CREATED)

    
    
class ipa_View(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        # data = request.data
        text = request.data.get('text')
        # print('================' , text)
        if text:
            transcription = ipa.convert(text)
            return Response({ 
                'Status:': 'Success',
                'transcription': transcription
            }, status=status.HTTP_200_OK)
            
        else:
            return Response(
                {'message': 'you should enter text'}, 
                status=status.HTTP_400_BAD_REQUEST
            )


# class GTS(APIView):
    
#     def post(self, request):
#         # data = request.data
#         text = request.data.get('text')
#         # print('================' , text)
#         if text:
#             transcription = ipa.convert(text)
#             return Response({ 
#                 'Status:': 'Success',
#                 'transcription': transcription
#             }, status=status.HTTP_200_OK)
            
#         else:
#             return Response(
#                 {'message': 'you should enter text'}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )