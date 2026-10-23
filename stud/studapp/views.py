from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from studapp.models import StudentDb

# Create your views here.
class StudentList(APIView):
    def get(self, request):
        qs = StudentDb.objects.all().values()
        result = list(qs)
        return Response(data=result)
    def post(self,request):
        form_data=request.data
        StudentDb.objects.create(**form_data)
        return Response({"message":"Added successfully..!"})