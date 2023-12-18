from django.urls import path
from . import views

urlpatterns = [
    path('studenthome/', views.studentHome, name='studenthome'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]