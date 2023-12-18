"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login import views as login_views
from django.conf.urls import handler404
from not_found.views import not_found_404

handler404 = not_found_404


urlpatterns = [
    path('',login_views.login,name='login'),
    path('admin/', admin.site.urls),
    path('',include('login.urls')),
    path('',include('no_access.urls')),
    path('',include('not_found.urls')),
    path('',include('studenthome.urls')),
    path('',include('teacherhome.urls')),
    path('login/',include('login.urls')),
]

