from django.contrib import admin
from django.urls import path

from smart_vaccine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login_user, name='login'),
    path('registration/', views.register_user, name='registration'),
    path('user/', views.user, name='user')
]
