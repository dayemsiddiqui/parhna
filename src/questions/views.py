from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import Question, Answer
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, "explore.html", {})

def ask_question(request):
    if request.user.is_authenticated():
        return render(request, "ask.html", {})
    else:
        return HttpResponseRedirect("/questions")

def answer(request, q_id):
    if request.method == 'POST':
        if request.user.is_authenticated():
            answer = Answer(answer=request.POST.get("answer"), question=Question.objects.get(question_id=q_id), author=request.user, votes=0)
            answer.save()
            print "Answer Save"
            return HttpResponseRedirect("/questions/"+str(q_id))
    else:
        return HttpResponseRedirect("/accounts/auth")


def get_question(request, q_id):

    question = Question.objects.get(question_id=q_id)

    try:
        answers = Answer.objects.filter(question=question)
        print "Found something"
    except Answer.DoesNotExist:
        answers = None

    context = {
        'question': question,
        'answers': answers
    }
    return render(request, "questions.html", context)

# ===========================================
#     Information Processing Functions
# ===========================================


def save(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            question = Question(title=request.POST.get("title"), description=request.POST.get("description"), author=request.user.username, votes=0)
            question.save()
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

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
            response[i]['id'] = question.question_id
            response[i]['title'] = question.title
            response[i]['description'] = question.description
            response[i]['author'] = question.author
            response[i]['votes'] = question.votes
            print "================"
            i = i + 1
        return JsonResponse(response)
