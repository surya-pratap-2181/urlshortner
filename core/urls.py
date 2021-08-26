from django.urls import path
from core import views
urlpatterns = [
    path('', views.shortner, name='short'),
    # path('', views.home, name='home'),
]
