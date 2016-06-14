from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from .models import SignUp
# Create your views here.


def index(request):
    title = "Parhna is coming soon subscribe to our newsletter"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            subscriber = SignUp(email=form.cleaned_data['email'], full_name=form.cleaned_data['name'])
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


def pindex(request):
    title = "Parhna is coming soon subscribe to our newsletter"
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        subscriber = SignUp(email=form.cleaned_data['email'], full_name=form.cleaned_data['name'])
        subscriber.save()
        print "New subscriber added"
        messages.success(request, "You have been subscribed")

        return HttpResponseRedirect('/newsletter/')

    context = {
        "template_title": title,
        "form": form,
    }
    return render(request, "subscribe.html", context)
