from django.urls import path
from . import views

urlpatterns = [
    path('not_found/', views.not_found, name='not_found'),
]