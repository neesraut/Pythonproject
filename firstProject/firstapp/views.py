from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

class view1(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class view2(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is my b view')