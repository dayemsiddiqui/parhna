from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            print "You have been registered sucessfully"
            return HttpResponseRedirect("/accounts/login")
        else:
            return render(request, "index.html", {'form' : form})
            print form.errors
    else:
        return HttpResponseRedirect("/")

#Displays the login page
def signin(request):
    return render(request, "login.html", {})

#Logout the user
def signout(request):
    logout(request)
    return HttpResponseRedirect("/")

#Authenticates the user and takes them to the dashboard
def profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return display_profile(request)
            else:
                print "Your account is not active yet!"
                # Return a 'disabled account' error message
        else:
            print "Invalid username or password"
            return HttpResponseRedirect("/accounts/login")
    else:
        if request.user.is_authenticated():
                return display_profile(request)
        else:
            return HttpResponseRedirect("/accounts/login")


#display and render dashboard
def display_profile(request):
    context = {
    'username': request.user.username,
    'email': request.user.email
    }
    return render(request, "profile.html", context)
