from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from smart_vaccine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login_user/', views.login_user, name='login_user'),
    path('registration/', views.register_user, name='registration'),
    path('account/', views.user, name='account'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
