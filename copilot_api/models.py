from django.db import models


class Resume(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100, blank=True, default='')
    firstname = models.CharField(max_length=100, blank=True, default='')
    lastname = models.CharField(max_length=100, blank=True, default='')
    education = models.TextField(default='')
    work_experience = models.TextField(default='')
    parsed_resume = models.JSONField()
    file = models.FileField(default='')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    parsed = models.BooleanField(default=False)
    resume_insight = models.JSONField(blank=True, default=dict)

    def __str__(self):
        return self.uploaded_on.date()

    class Meta:
        ordering = ['created']
