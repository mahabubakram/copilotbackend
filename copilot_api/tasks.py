# tasks.py
import os

from celery import shared_task

from copilot_api.gptQuery.gptCommons import GPTQuery
from copilot_api.models import Resume
from fileupload.tasks.resumeparser import ResumeParser


def GptTaskResumeInsight(gpt, resume):
    gpt.process(resume)
    print(gpt.get_result())
    return gpt.get_result()


@shared_task
def resume_parser(arg1, arg2):
    system_prompt = """Act as a resume parser agent. 
    You will be given a resume, detect the language and give me the list of professional experiences from the resume in the same language, including their employer details and detail work experiences.
    Your output should be a valid json object. List the extracted responsibilities as a list."""
    resumeGPT = GPTQuery(system_prompt)

    # Task logic here
    resumes = Resume.objects.filter(parsed=False)
    for resume in resumes:
        parsed_resume = ResumeParser.resumeparser(resume.file.name)
        resume.parsed_resume = parsed_resume
        resume.resume_insight = GptTaskResumeInsight(resumeGPT, resume.parsed_resume)
        resume.parsed = True
        resume.save()
    return None
