from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
        print "You have been registered sucessfully"
        return render(request, "subscribe.html", {})
