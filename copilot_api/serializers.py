from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ["parsed_resume", "file", "uploaded_on", "parsed", "resume_insight", "user_id", "submitted_form_data",
                  "submitted_pdf_url", "email", "submitted_pdf_path"]
