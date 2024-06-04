# admin.py
from django.contrib import admin
from .models import User, Vaccine, Vaccinations, Child


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass


@admin.register(Vaccinations)
class VaccinationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    pass
