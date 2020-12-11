from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from  firstapp.models import Users
from .forms import UsersForm

from django.contrib.auth.models import User

##formcontent
from django.contrib.auth.forms import UserCreationForm

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
        return HttpResponse(user_list)

##simpler form of views
def displayUsers(request):
    users_list = Users.objects.all().values()
    template = 'home.html'
    content = {
        'users' : users_list


    }
    return render(request,template,content)

def signUp(request):
    template = "signUp.html"
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        print('oh no')
        form = UserCreationForm()
    content={
        'form' : form
    }
    

    return render(request, template, content)

##this is logged in user -admin user
def profile_edit(request):
    
    template = "profile_edit.html"
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm(instance = request.user)
    content={
        'form' : form
    }
    

    return render(request, template, content)

##this is dynamic user
def dynamicUser_edit(request,id):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm(instance = User.objects.get(id=id))
    content={
        'form' : form
    }
    template = "profile_edit.html"
    return render(request, template, content)


def success(request):
    template = 'success.html'
    return render(request,template)

##custom Model Form, for custom users
def cusmodel_users(request):
    template = 'users.html'

    if request.method =="POST":
        form = UsersForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        form = UsersForm(instance=request.user)

    content = {
        'form': form
    }
    return render(request, template, content)
