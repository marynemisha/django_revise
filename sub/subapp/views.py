from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class SubView(View):
    def post(self,request):
        request_body=request.body
        data=loads(request_body)
