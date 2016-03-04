from django.shortcuts import render
from django.http import HttpResponse
from userprofiles.forms import RegistrationForm
# Create your views here.
def index(request):
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "index.html", context)
