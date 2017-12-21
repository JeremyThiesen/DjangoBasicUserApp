from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django import forms

from user.models import *
# Create your views here.

def my_login_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if not (request.user and request.user.is_authenticated()):
            return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            return function(request, *args, **kw)
    return wrapper


def UserLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('user:profile'))
            # Redirect to a success page.
        else:
            pass
            # Return a 'disabled account' error message
    else:
        return HttpResponseRedirect(reverse('user:login'))


def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@my_login_required
def UserProfile(request):
    message = request.GET.get('message','')
    if message == 'email':
        message = 'Email sent successfully!'

    return render(request, 'user/profile.html', {'message':message})


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
    

def uploadPic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.picture = form.cleaned_data['image']
            request.user.save()
    
        return HttpResponseRedirect(reverse('user:profile'))
        
    else:    
        return HttpResponseForbidden('allowed only via POST')
