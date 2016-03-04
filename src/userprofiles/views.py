from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print "You have been registered sucessfully"
            return render(request, "subscribe.html", {})
        else:
            print form.errors

def profile(request):
    return render(request, "profile.html", {})
