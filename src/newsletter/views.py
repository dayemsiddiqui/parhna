from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
# Create your views here.
def index(request):
    title = "Parhna is coming soon subscribe to our newsletter"
    form = SignUpForm(request.POST)

    if form.is_valid():
        instance = form.save(commit=False)
        print instance
    context = {
        "template_title": title,
        "form": form
    }
    return render(request, "subscribe.html", context)
