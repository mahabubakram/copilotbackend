# scheduler.py
import os
import json
import requests
from django.http import HttpResponse

from celery import shared_task

from copilot_api.gptQuery.gptCommons import CreateGPTQuery
from copilot_api.models import Resume
from copilotbackend.settings import MEDIA_ROOT
from fileupload.tasks.resumeparser import ResumeParser


def GptTaskResumeInsight(prompt):
    gptQuery = CreateGPTQuery(prompt)
    prompt = prompt + os.linesep \
             + "from the text above, detect the language and give me the list of professional experiences in the same language, " \
               "including their employer details and detail work experiences. " \
               "make it as a json object but list the responsibilites as a list." \
               "also provide personal information as an object," \
               "provide education as an object," \
               "provide skills as an object" \
               "and also other certifications and rewards as an object"
    gptQuery.PROMPT = prompt
    gptQuery.generate()
    print(gptQuery.get_result())
    return gptQuery.get_result()


def download_file(resume: Resume):
    response = requests.get(resume.submitted_pdf_url)

    if response.status_code == 200:
        # Set the file name for the downloaded file
        filename = 'resume.pdf'

        # Create an HttpResponse with the file content and appropriate headers
        response = HttpResponse(
            response.content,
            content_type='application/octet-stream'
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        file = os.path.join(MEDIA_ROOT, filename)
        file = open(file, "wb")
        file.write(response.content)
        file.close()

        return file;
    else:
        return HttpResponse("Failed to download the file.")
@shared_task
def resume_parser(arg1, arg2):
    # Task logic here
    resumes = Resume.objects.filter(parsed=False)
    for resume in resumes:
        file_response = download_file(resume)
        parsed_resume = ResumeParser.resume_parser(file_response)

        resume.parsed_resume = json.loads(parsed_resume)
        resume.resume_insight = json.loads(GptTaskResumeInsight(parsed_resume))
        resume.parsed = True
        resume.save()
    return None
