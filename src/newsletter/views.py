from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
from .models import SignUp
# Create your views here.
def index(request):
    title = "Parhna is coming soon subscribe to our newsletter"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            subscriber = SignUp(email = form.cleaned_data['email'], full_name=form.cleaned_data['name'])
            subscriber.save()
            print "New subscriber added"
        return render(request, 'index.html', {})
    else:
        form = SignUpForm()
        context = {
            "template_title": title,
            "form": form
        }
        return render(request, "subscribe.html", context)
