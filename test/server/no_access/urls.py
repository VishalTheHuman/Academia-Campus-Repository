from django.urls import path
from . import views

urlpatterns = [
    path('no_access/', views.no_access, name='no_access'),
]