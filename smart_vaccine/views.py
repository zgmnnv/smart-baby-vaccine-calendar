from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from .models import Child, Vaccinations
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import User as CustomUser
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
        child = request.POST['baby-name']
        password = request.POST['password']

        # Создаем пользователя и сохраняем в базу
        registered_user = CustomUser(username=name, email=email, childname=child)
        registered_user.set_password(password)
        registered_user.save()

        # Создаем запись о ребенке пользователя и сохраняем в базу
        child = Child(name=child, birth_date=request.POST['dob'], gender=request.POST['gender'],
                      country=request.POST['country'], parent_id=CustomUser.objects.get(pk=registered_user.pk))
        child.save()

        return render(request,'welcome.html')

    return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        user_email = request.POST.get('user-email')
        password = make_password(request.POST.get('password'))  # Хэшируем введенный пароль
        user_auth = authenticate(request, username=user_email, password=password)

        if user_auth is not None:
            login(request, user_auth)
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
