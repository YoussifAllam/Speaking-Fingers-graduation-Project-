from django.urls import path
from .views import SpeechAnalysisView

urlpatterns = [
    path('analyze/', SpeechAnalysisView.as_view(), name='speech_analysis'),
]
