# tasks.py
import os

from celery import shared_task

from copilot_api.gptQuery.gptCommons import CreateGPTQuery
from copilot_api.models import Resume


def GptTaskResumeInsight(prompt):
    gptQuery = CreateGPTQuery(prompt)
    prompt = prompt + os.linesep \
             + "can you tell me what are the professional experience from these texts above. It can be in German language the whole texts above"
    gptQuery.PROMPT = prompt
    gptQuery.generate()
    print(gptQuery.get_result())
    return gptQuery.get_result()


@shared_task
def resume_parser(arg1, arg2):
    # Task logic here
    resumes = Resume.objects.filter(parsed=False)
    for resume in resumes:
        resume.resume_insight = GptTaskResumeInsight(resume.parsed_resume)
        resume.parsed = True
        resume.save()
    return None
