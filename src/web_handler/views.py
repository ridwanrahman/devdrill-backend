from django.shortcuts import render, HttpResponse
from models.models import User, Category, UserQuestion, Question

def home_page(request):
    questions = Question.objects.all()
    return HttpResponse({"response": "i hope this works"})
    # return render(request, "home.html", {"questions": questions})
