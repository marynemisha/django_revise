from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class Addview(View):
    def post(self,request):
        data=request.body
        form_data=loads(data)
        x=form_data.get("n1")
        y=form_data.get("n2")
        result=x+y
        data={
            "Result":result
        }
        return JsonResponse(data)