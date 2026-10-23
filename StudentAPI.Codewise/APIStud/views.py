from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from APIStud.models import Student
from APIStud.serializers import StudentSerializer
# Create your views here.
class StudentListViewCreate(APIView):
    def get(self, request):
        qs = Student.objects.all()
        serializer_instance = StudentSerializer(qs, many=True)
        return Response(data=serializer_instance.data)
    def post(self, request):
        form_data = request.data
        serializer_instance = StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            Student.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class StudentView(APIView):
    def get(self, request, pk):
        qs = Student.objects.get(id=pk)
        serializer_instance = StudentSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Student.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self, request, pk):
        Student.objects.filter(id=pk).delete()

        return Response(
            {"message": "Student deleted successfully!"}
        )