from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def description(request):
    return render(request, 'generator/description.html')


def password(request):
    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list('!@£$%^&*_+'))
    if request.GET.get('numbers'):
        characters.extend(list(string.octdigits))
    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})
