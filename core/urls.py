from django.urls import path
from core import views
urlpatterns = [
    path('', views.home, name='home'),
    path('shorturl/', views.short_url, name='shorturl'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<str:query>', views.home, name='home'),
    path('delete_url/<int:id>', views.delete_url, name='delete_url'),
]
