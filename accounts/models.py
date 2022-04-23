
from django.db import models
from django.contrib.auth.models import User

class AboutUser(models.Model):
    first_name = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=55)
    adress = models.CharField(max_length=55)
    phone_nuadressmber = models.CharField(max_length=55)
    index = models.CharField(max_length=55)
    pin = models.IntegerField()

    def __str__(self):
        return self.first_name.username

    class Meta:
        verbose_name_plural = 'About Us'



# Create your models here.
