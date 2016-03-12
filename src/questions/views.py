from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import Question
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "ask.html", {})


def ask(request):
    return render(request, "questions.html", {})

def json_save(request):
    print "Hello"
    if request.method == 'POST':
        if request.user.is_authenticated():
            data = json.loads(request.body)
            question = Question(title=data['title'], description=data['description'], author=request.user.username, votes=0)
            question.save()
            response = {'status': "Thanks for asking the question"}
            return JsonResponse(response)
        else:
            print "You are not logged in!"
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def json_get(request):
        questions = Question.objects.all()
        response = {}
        i = 0
        for question in questions:
            response[i] = {}
            print "================"
            response[i]['title'] = question.title
            response[i]['description'] = question.description
            response[i]['author'] = question.author
            response[i]['votes'] = question.votes
            print "================"
            i = i + 1
        return JsonResponse(response)
