from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from  firstapp.models import Users

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
    print("yayayyayayya")
    template = "signUp.html"

    if request =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm()
    content={
        'form' : form
    }
    

    return render(request, template, content)

def success(request):
    template = 'success.html'
    return render(request,template)