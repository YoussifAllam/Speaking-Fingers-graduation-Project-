# hand_tracking_app/serializers.py
from rest_framework import serializers

class FrameSerializer(serializers.Serializer):
    frame = serializers.CharField()
