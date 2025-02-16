from django.shortcuts import render
from models.models import User, Category, UserQuestion, Question

def home_page(request):
    questions = Question.objects.all()
    return render(request, "home.html", {"questions": questions})
