from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
# from ultralytics import YOLO
# import torch

# Set device to CPU

class HandTrackingAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # device = torch.device('cpu')
        l = torch.cuda.is_available()

        return Response({
                         'Status:':'Success',
                         'sign_language_numbers': 1
                         })

# Create your views here.
