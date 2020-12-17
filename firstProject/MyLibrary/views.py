from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  firstapp.models import Users
from django.contrib.auth.models import User

##formcontent
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

def libraryHome(request):
    template = "mylibrarytemplate/manage/pages/home.html"
    return render(request, template)