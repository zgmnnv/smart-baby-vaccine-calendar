from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    child_name = models.CharField(max_length=50, blank=True, unique=False)

    class Meta:
        unique_together = [['username']]  # Убираем уникальность username


class Vaccine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=False)
    description = models.CharField(max_length=300, unique=False)
    min_age_in_month = models.IntegerField(unique=False)


class Vaccinations(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(unique=False)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE)


class Child(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=50, default='Boy')
    country = models.CharField(max_length=50, default='Russia')
    parent_id = models.ForeignKey(User, on_delete=models.CASCADE)
    next_vaccine_id = models.CharField(max_length=50, null=True)
    last_vaccination_id = models.ForeignKey(Vaccinations, on_delete=models.CASCADE, null=True)
    next_vaccine_date = models.DateTimeField(null=True)
    last_vaccine_date = models.DateTimeField(null=True)
