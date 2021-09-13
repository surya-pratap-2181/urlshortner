from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
import random
import string
from django.contrib import messages
from .models import CustomUser

# Create your views here.


def random_invite():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(8))


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


def register_request(request, invite="shortly"):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password2 = form.cleaned_data.get("password2")
            mobile_number = form.cleaned_data.get("mobile_number")
            email = form.cleaned_data.get("email")
            invited_by = form.cleaned_data.get("invited_by")
            invite_query = random_invite()
            user = CustomUser.objects.create_user(username=username, password=password2, email=email,
                                                  mobile_number=mobile_number, invited_by=invited_by, invite_query=invite_query)
            user.save()
            messages.success(request, "Registration successful.")
            return redirect("/accounts/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm(initial={"invited_by": invite})
    return render(request, "accounts/register.html", {"form": form})


def profile_page(request):
    return redirect('/shorturl/')
    # return render(request, 'accounts/profile.html')


def user_logout(request):
    logout(request)
    return redirect('/accounts/')
