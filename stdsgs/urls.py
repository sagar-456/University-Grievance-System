"""
URL configuration for stdsgs project.

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
from django.urls import path, include
from grievance import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home/',views.home),
    path('contact/',views.contact),
    path('about/',views.about),
    path('',include('django.contrib.auth.urls')),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/',views.logout_user, name='logout_user'),
    path('register_user/',views.register_user, name='register_user'),
    path('profile/',views.profile, name='profile'),
    path('guidelines/',views.guidelines),
    path('notice/',views.notice),
    path('usernotice/',views.usernotice),
    
    
]
