from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
import json

# Create your views here.

def auth(request):
    return render(request, "auth.html", {})

def register(request):
    if request.method == 'POST':
        # Todo data validation
        if True:
            user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
            user.save()
            profile = UserProfile(user=user)
            profile.save()
            print "You have been registered sucessfully"
            return HttpResponseRedirect("/accounts/login")
        else:
            return render(request, "index.html", {})
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


#Profile Display and editing
def editprofile(request):
    if request.user.is_authenticated():
        context = {
        'username': request.user.username,
        'email': request.user.email
        }
        return render(request, "profileinfo.html", context)
    else:
        return HttpResponseRedirect("/")


# =================================
#           HELPER METHODS
# =================================
#display and render dashboard
def display_profile(request):
    context = {
    'username': request.user.username,
    'email': request.user.email
    }
    return render(request, "profile.html", context)



# =================================
#           JSON API
# =================================
def json_getprofile(request):
    if request.user.is_authenticated():
        profile =  UserProfile.objects.get(user=request.user)
        response = {'email':request.user.email,
                    'username': request.user.username,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'institute': profile.institute}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect("/")

# Saves data to the database
def json_saveprofile(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            data = json.loads(request.body)
            print data
            userprofile = UserProfile.objects.get(user = request.user)
            userprofile.institute = data['institute']
            userprofile.save()
            request.user.first_name = data['first_name']
            request.user.last_name = data['last_name']
            request.user.save()
            response = {'status': "Your profile was saved successfully"}
            return JsonResponse(response)
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
