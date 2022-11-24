from atexit import register
from django import template
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.models import Group

register = template.Library()


@register.filter
def replaceBlank(value,stringVal = ""):
    value = str(value).replace(stringVal, '')
    return value

@register.filter
def encryptdata(value):
    fernet = Fernet(settings.ID_ENCRYPTION_KEY)
    value = fernet.encrypt(str(value).encode())
    return value

#Consultar grupo do User
@register.filter(name='is_group')
def is_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False