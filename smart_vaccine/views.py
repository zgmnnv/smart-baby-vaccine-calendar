from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from .models import User, Child, Vaccinations
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return TemplateResponse(request, "index.html")

#@login_required
def user(request):
    return TemplateResponse(request, "user.html")

def welcome(request):
    return TemplateResponse(request, "welcome.html")

def register_user(request):
    if request.method == 'POST':
        name = request.POST['your-name']
        email = request.POST['email']
        child_name = request.POST['baby-name']
        password = request.POST['password']

        # Создаем пользователя и сохраняем в базу
        user = User(username=name, email=email, child_name=child_name, password=password)
        user.save()

        # Создаем запись о ребенке пользователя и сохраняем в базу
        child = Child(name=child_name, birth_date=request.POST['dob'], gender=request.POST['gender'],
                      country=request.POST['country'], parent_id=User.objects.get(pk=user.id))
        child.save()

        return render(request,'welcome.html')

    return render(request, 'registration.html')

def login_user(request):
    if request.method == 'POST':
        user_email = request.POST.get('user-email')
        password = request.POST.get('password')
        user = authenticate(request, username=user_email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'user.html')  # Отображение страницы user.html после успешной авторизации
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
            return redirect('login_user')  # Перенаправление на страницу логина в случае неверных учетных данных
    else:
        return render(request, 'login.html')

def child_dashboard(request):
    user = request.user
    try:
        child = Child.objects.get(parent_id=user.id)
        next_vaccine = Vaccinations.objects.get(id=child.next_vaccine_id)
        last_vaccine = Vaccinations.objects.get(id=child.last_vaccination_id)
    except Child.DoesNotExist:
        child = None
        next_vaccine = None
        last_vaccine = None

    context = {
        'child': child,
        'next_vaccine': next_vaccine,
        'last_vaccine': last_vaccine,
    }

    return render(request, 'user.html', context)