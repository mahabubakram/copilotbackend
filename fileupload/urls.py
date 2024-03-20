from django.urls import path, include

from fileupload.views import FileUploadAPIView

urlpatterns = [
    path('api', FileUploadAPIView.as_view()),
]