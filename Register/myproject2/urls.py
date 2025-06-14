"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# myproject/myproject/urls.py

from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views  # Import views from accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.login, name='login'),
    path('signup_success/', accounts_views.signup_success, name='signup_success'),
    path('', accounts_views.index, name='index'),  # Default route for the homepage
]

