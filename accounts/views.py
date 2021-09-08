from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import LoginForm, RegisterForm

# Create your views here.


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


def profile_page(request):
    return redirect('/shorturl/')
    # return render(request, 'accounts/profile.html')


def user_logout(request):
    logout(request)
    return redirect('/accounts/')
