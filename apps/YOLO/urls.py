from django.urls import path , include

from django.conf import settings
from .views import *

urlpatterns = [ 
               
    path('hand-tracking/', HandTrackingAPI.as_view(), name='hand_tracking_api'),
]