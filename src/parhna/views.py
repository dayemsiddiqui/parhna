from django.shortcuts import render
from django.http import HttpResponse
from userprofiles.forms import RegistrationForm
# Create your views here.
def register(request):
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)

def index(request):
    return render(request, "index.html", {})
