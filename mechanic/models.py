from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Mechanic(models.Model):
    gender_options = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    specialization = (
        ('service-technician', 'Service-Technician'),
        ('brake-transmission-mechanic', 'Brake-Transmission-Mechanic'),
        ('general-mechanic', 'General-Mechanic'),
        ('diesel-mechanic', 'Diesel-Mechanic'),
        ('electro-mechanic', 'Electro-Mechanic'),
        ('body-mechanic', 'Body-mechanic'),
        ('office', 'Office'),
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    active = models.BooleanField(default=True)
    specialization = models.CharField(choices=specialization, max_length=27)
    gender = models.CharField(choices=gender_options, max_length=6)
    profile = models.ImageField(upload_to='profiles/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
