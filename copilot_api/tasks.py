# tasks.py
import os

from celery import shared_task

from copilot_api.gptQuery.gptCommons import CreateGPTQuery
from copilot_api.models import Resume
from fileupload.tasks.resumeparser import ResumeParser


def GptTaskResumeInsight(prompt):
    gptQuery = CreateGPTQuery(prompt)
    prompt = prompt + os.linesep \
             + "from the text above, detect the language and give me the list of professional experiences in the same language, " \
               "including their employer details and detail work experiences. " \
               "make it as a json object but list the responsibilites as a list."
    gptQuery.PROMPT = prompt
    gptQuery.generate()
    print(gptQuery.get_result())
    return gptQuery.get_result()


@shared_task
def resume_parser(arg1, arg2):
    # Task logic here
    resumes = Resume.objects.filter(parsed=False)
    for resume in resumes:
        parsed_resume = ResumeParser.resumeparser(resume.file.name)
        resume.parsed_resume = parsed_resume
        resume.resume_insight = GptTaskResumeInsight(resume.parsed_resume)
        resume.parsed = True
        resume.save()
    return None
