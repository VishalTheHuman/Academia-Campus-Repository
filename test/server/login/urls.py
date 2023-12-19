from django.urls import path, include
from login import views as login_views  # Use an alias for the login views
from . import views as app_views  # Use an alias for the app views

urlpatterns = [
    path('login/', login_views.login, name='login'),
    path('login_view/', login_views.login_view, name='login_view'),
    path('signup/', app_views.signup_view, name='signup'),
    path('forgot_password/', app_views.forgot_password, name='forgot_password'),
]