from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
    return TemplateResponse(request, "index.html")

def login(request):
    return TemplateResponse(request, "login.html")

#@login_required
def user(request):
    return TemplateResponse(request, "user.html")

def registration(request):
    return TemplateResponse(request, "registration.html")