from django.contrib import admin
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    
    path('api/', include('apps.Users.urls')),
    path('api/CNN-api/', include('apps.CNN.urls')),
    path('api/v1/Mediapipe/', include('apps.Mediapipe.urls')),
    path('api/v1/YOLO/', include('apps.YOLO.urls')),
    path('api/v1/GTTS/', include('apps.GTTS.urls')),
    path('api/v1/Videos/', include('apps.Videos.urls')),
    path('Levels/', include('apps.Levels.urls')),
    path('api/v1/SpeechAnalysis/', include('apps.GP.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
