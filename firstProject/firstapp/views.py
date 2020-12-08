from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from  firstapp.models import Users

from django.shortcuts import render, get_object_or_404, redirect
class view1(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class view2(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is my b view')

class GetUsers(View):


    def get(self, request, *args, **kwargs):
        
        user_list = Users.objects.all().values()
        print(user_list)
        return HttpResponse(user_list)