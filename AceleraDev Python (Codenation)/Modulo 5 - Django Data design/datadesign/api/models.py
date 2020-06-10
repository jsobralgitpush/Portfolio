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


class Agent(models.Model):
    name = models.CharField('name', max_length=50, null=True)
    status = models.BooleanField('status', null=True)
    env = models.CharField('env', max_length=20, null=True)
    version = models.CharField('version', max_length=5, null=True)
    address = models.CharField('address', max_length=39, null=True, validators=[validate_ipv4_address])


class Group(models.Model):
    name = models.CharField('name', max_length=50, null=True)

class Event(models.Model):
    #Na documentação, ele sugere colocarmos as "opções" em forma de tupla sendo:
    # a) O primeiro argumento a opção em forma de string que será colocada pelo user
    # b) O segundo argumento uma string com a "explicação" (human-readable) do campo.
    LEVEL_CHOICES = [('CRITICAL','CRITICAL'), ('DEBUG','DEBUG'), ('ERROR','ERROR'),
                     ('WARNING','WARNING'), ('INFO','INFO')]

    level = models.CharField('level', max_length=50, choices=LEVEL_CHOICES)
    data = models.TextField('data', null=True)
    arquivado = models.BooleanField('arquivado', null=True)
    date = models.DateField('date', null=True, auto_now_add=True)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.DO_NOTHING
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )

class GroupUser(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING

    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING

    )