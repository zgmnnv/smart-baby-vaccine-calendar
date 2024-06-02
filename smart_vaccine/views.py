from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Child
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Child, Vaccinations

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

def register_user(request):
    if request.method == 'POST':
        name = request.POST['your-name']
        email = request.POST['email']
        child_name = request.POST['baby-name']
        password = request.POST['password']

        # Создаем пользователя и сохраняем в базу
        user = User(name=name, email=email, child_name=child_name, password=password)
        user.save()

        # Создаем запись о ребенке пользователя и сохраняем в базу
        child = Child(name=child_name, birth_date=request.POST['dob'], gender=request.POST['gender'],
                      country=request.POST['country'], parent_id=User.objects.get(pk=user.id))
        child.save()

        return HttpResponse('Вы успешно зарегистрированы!')

    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Добро пожаловать. Вы вошли как {username}.")
                return render('user.html')
            else:
                messages.error(request, "Неверное имя пользователя или пароль.")
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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

    return render(request, 'user_dashboard.html', context)