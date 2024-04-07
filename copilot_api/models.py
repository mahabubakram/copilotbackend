from django.db import models


class Resume(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    parsed_resume = models.JSONField()
    file = models.FileField(default='')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    parsed = models.BooleanField(default=False)
    resume_insight = models.JSONField(blank=True, default=dict)
    user_id = models.IntegerField(blank=True, default='')
    submitted_form_data = models.JSONField(blank=True, default=dict)
    submitted_pdf_url = models.FileField(blank=True, default='')
    email = models.EmailField(blank=True, default='')
    submitted_pdf_path = models.FileField(blank=True, default='')

    def __str__(self):
        return self.uploaded_on.date()

    class Meta:
        ordering = ['created']
