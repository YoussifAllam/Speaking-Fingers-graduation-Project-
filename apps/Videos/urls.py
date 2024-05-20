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
    
    path('Get_All_Videos/', VideoListView.as_view({'get': 'list'})),
    path('Get-Video-Details/', get_video_details, name='get_video_details'),
    path('Get-user-favorites-videos/', FavoriteVideoListCreateView.as_view(), name='favorite-list-create'),
    path('add-fav-video-to-user/' , favorite_video ),
    path('remove-favorite-video/', remove_favorite_video, name='remove_favorite_video'),
    

]