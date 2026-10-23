from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Myclass(APIView):
    def get(self,request):
        return Response({"message":"Good morning..!"})

class AdditionView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x+y
        return Response({"result":result})

class SubView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x-y
        return Response({"result":result})

class MulView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        result=x*y
        return Response({"result":result})

class LargeView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        if x>y:
            return Response({"Largest":x})
        else:
            return Response({"Largest":y})

class TempView(APIView):
    def post(self,request):
        celsius=request.data.get("temp")
        F=(celsius*9/5)+32
        return Response({"Result":F})