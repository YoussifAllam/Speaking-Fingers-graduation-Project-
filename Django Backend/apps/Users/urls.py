from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView # , TokenObtainPairView
#app name 
app_name = 'Users'
router = DefaultRouter()
router.register(r'users', UserViewSet,basename='users') 
# router.register('videos', VideoListView)
# router.register('Video-Details', VideoDetailView)

# path('favorites/<int:pk>/', FavoriteVideoDestroyView.as_view(), name='favorite-destroy'),

urlpatterns = [
    
    path('', include(router.urls)),
    path('user/confirm-email/', UserViewSet.as_view({'post': 'confirm_email'}), name='confirm-email'),
    path('user/resend-otp/', UserViewSet.as_view({'post': 'send_reset_otp'}), name='send-reset-otp'),
    path('user/login/', CustomTokenObtainPairView.as_view(), name='user-login'),
    
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('userinfo/', current_user,name='user_info'), 
    path('userinfo/update/', update_user,name='update_user'), 
    
    path('forgot_password/', forgot_password,name='forgot_password'), 
    path('reset_password/<str:token>',reset_password,name='reset_password'), 
    
    path('user/logout/', APILogoutView.as_view(), name='logout_token'),
    
    #!__________________________________________________________________________________
    # path('videos/', VideoListView.as_view(), name='video-list'),
    # path('video-detail/', get_video_details),
    
    # path('favorites/', FavoriteVideoListCreateView.as_view(), name='favorite-list-create'),
    # path('favorites/<int:video_id>/remove/', FavoriteVideoDestroyView.as_view(), name='remove-favorite-video'),

]