# coplitobackend/copilot_api/urls.py : API urls.py
from django.urls import path, include
from .views import (
    ResumeListApiView,
)

urlpatterns = [
    path('api', ResumeListApiView.as_view()),
]