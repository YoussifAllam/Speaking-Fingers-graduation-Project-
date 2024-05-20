from django.urls import path , include
from .views import * 
# #app name 
# app_name = 'Users'
# router = DefaultRouter()
# router.register(r'users', UserViewSet,basename='users') 
# router.register('videos', VideoListView)
# router.register('Video-Details', VideoDetailView)

# path('favorites/<int:pk>/', FavoriteVideoDestroyView.as_view(), name='favorite-destroy'),

urlpatterns = [
    
    path('IPA/', ipa_View.as_view()),
    path('text-to-speech/', TextToSpeechAPI.as_view(), name='text-to-speech'),

    
]