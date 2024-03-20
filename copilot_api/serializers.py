from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["address", "firstname", "lastname", "education", "work_experience", "parsed_resume", "file",
                  "uploaded_on"]
