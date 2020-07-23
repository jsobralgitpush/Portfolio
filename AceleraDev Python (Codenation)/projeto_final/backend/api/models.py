from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_ipv4_address

# Create your models here.
class User(models.Model):
    name = models.CharField('name', max_length=50, null=True)
    last_login = models.DateField('last_login', auto_now=True)
    email = models.CharField('email', max_length=254, validators=[EmailValidator()])
    password = models.CharField('password', max_length=50, validators=[MinValueValidator(8)])

class Error(models.Model):
    log = models.CharField('log', max_length=50, null=True)
    date_event = models.DateField('date', auto_now=True)

