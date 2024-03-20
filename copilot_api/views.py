from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework import permissions

from fileupload.tasks.resumeparser import ResumeParser
from .models import Resume
from .serializers import ResumeSerializer
from .tasks import resume_parser


class ResumeListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ResumeSerializer

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the resume items for given requested user
        '''
        print("calling the task")
        resume_parser.delay(3, 5)
        print("calling done")
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Resume with given resume data
        '''
        data = {
            'address': request.data.get('address'),
            'firstname': request.data.get('firstname'),
            'lastname': request.data.get('lastname'),
            'education': request.data.get('education'),
            'work_experience': request.data.get('work_experience'),
            'file': request.data.get('file'),
        }
        data['parsed_resume'] = "null"

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
