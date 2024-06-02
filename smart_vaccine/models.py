from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    child_name = models.CharField(max_length=50)
    
class Vaccine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=300)
    min_age_in_month = models.IntegerField()
    
class Vaccinations(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    
class Child(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    birth_date = models.DateTimeField()
    gender = models.IntegerField
    country = models.IntegerField
    parent_id = models.ForeignKey(User, on_delete=models.CASCADE)       
    next_vaccine_id = models.CharField(max_length=50)
    last_vaccination_id = models.ForeignKey(Vaccinations, on_delete=models.CASCADE)
    next_vaccine_date = models.DateTimeField()
    last_vaccine_date = models.DateTimeField()