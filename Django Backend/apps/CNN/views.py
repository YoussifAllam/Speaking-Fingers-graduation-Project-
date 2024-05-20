from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageSerializer
from .models import Image
from .tasks import classify_image

from rest_framework.permissions import IsAuthenticated



class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid():
            image_serializer.save()
            # print("______________________________Serializer Data:",image_serializer.data)
            image = Image.objects.get(id=image_serializer.data['id'])
            # Assume classify_image is a function that takes an image file and returns the class
            
            arabic_letter  = classify_image(image.picture)
            # print('------------------' , image.picture)
            json = {
                "status": "success",
                "data": {
                    "arabic_letter": arabic_letter 
                }
            }
            return Response(json , status=200)
        else:
            return Response(image_serializer.errors, status=400)
