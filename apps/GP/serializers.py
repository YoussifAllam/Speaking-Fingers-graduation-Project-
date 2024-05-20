from rest_framework import serializers
from .models import *
class AudioFileSerializer(serializers.Serializer):
    audio_file = serializers.FileField()
    reference_text = serializers.CharField()

class AudioFile_upload_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Audio_Model
        fields = ['id', 'Audio', 'uploaded_at']
