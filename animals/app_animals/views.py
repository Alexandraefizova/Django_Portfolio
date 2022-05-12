from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Animal
from .serializers import AnimalSerializer
from django.views.generic import ListView, DetailView, CreateView
from .forms import AnimalsForm, UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'animals/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'animals/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeList(ListView):
    model = Animal
    template_name = 'animals/home_page.html'
    context_object_name = 'animals'


class AnimalsDetailView(DetailView):
    model = Animal
    template_name = 'animals/animals_detail.html'
    context_object_name = 'animals'


class CreateAnimals(LoginRequiredMixin, CreateView):
    form_class = AnimalsForm
    template_name = 'animals/add_animals.html'
    success_url = '/'
    login_url = '/admin/'


def delete_animals(request):
    animals = Animal.objects.all()
    if request.user.is_authenticated:
        animals.delete()
        messages.success(request, 'Вы успешно удалили записи')
        return redirect('home')
    else:
        messages.error(request, 'Недостаточно прав для выполнения действия')
        return redirect('login')


class AnimalAPIList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AnimalAPIUpdate(generics.UpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAuthenticated,)


class AnimalAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAuthenticated,)
