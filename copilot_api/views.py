from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status

from .models import Resume
from .serializers import ResumeSerializer
from .resumeParsing import resume_parser
from supabase import create_client, Client
supabase: Client = create_client("https://kexddhjgsuypqmvxhnoy.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtleGRkaGpnc3V5cHFtdnhobm95Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwNjcxNjQ2NiwiZXhwIjoyMDIyMjkyNDY2fQ.oG3q-bW1xpYoCdtMLVaqvoXGd3m23S4jsGQ7ZcGUJBM")

## https://github.com/supabase-community/supabase-py

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
        get_resume_and_parse()
        resume_parser(3, 5)
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
            'file': request.data.get('file'),
            'user_id': request.data.get('user_id'),
            'email': request.data.get('email'),
        }
        # data['parsed_resume'] = ResumeParser.resumeparser("Lebenslauf_Akram_DE.pdf")

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
