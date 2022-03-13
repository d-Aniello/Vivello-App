from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginForm, RegistrationForm, UserPermissionForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('None')
        return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['pass_1'])
            user.save()
            return redirect('index')
        return render(request, 'register.html', {'form': form})


class UserPermissionView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermissionForm(instance=user)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermissionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})


class Users(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})
