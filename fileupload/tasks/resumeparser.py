import json
import os
import re
import fitz


from copilotbackend.settings import MEDIA_ROOT


class ResumeParser():

    def resumeparser(filename):
        data = {}
        file = os.path.join(MEDIA_ROOT, filename)
        doc = fitz.open(file)
        for page in doc:  # iterate the document pages
            text = page.get_text()  # get plain text encoded as UTF-8
            regex = "[ ]*(.+):[ ]*\n?((?:.+\n?[^\s])*)"
            dataPoints = re.search(regex, text, re.MULTILINE)
            # print(dataPoints)
            print(text)
            data[page.number] = text
        return json.dumps(data)

    def resume_parser(file):
        data = {}
        doc = fitz.open(file)
        for page in doc:  # iterate the document pages
            text = page.get_text()  # get plain text encoded as UTF-8
            regex = "[ ]*(.+):[ ]*\n?((?:.+\n?[^\s])*)"
            dataPoints = re.search(regex, text, re.MULTILINE)
            # print(dataPoints)
            print(text)
            data[page.number] = text
        return json.dumps(data)