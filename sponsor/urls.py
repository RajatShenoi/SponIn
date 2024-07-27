from django.urls import path
from . import views

app_name = 'sponsor'

urlpatterns = [
    path('register/', views.registerSponsor, name='register'),
]