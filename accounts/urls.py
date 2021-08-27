from django.urls import path
from accounts import views
from accounts.views import LoginView, RegisterView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]
