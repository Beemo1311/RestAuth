"""RestAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from accounts.views import (AllUserListApiView, AboutUserListApiView, AboutUserCreateApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # ---> Register/Reset Password/Reset Email/Reset Username/UserME
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),  # ----> Login/Logout
    path('api/v1/all_user/',  AllUserListApiView.as_view()),
    path('api/v1/create/about_user/', AboutUserCreateApiView.as_view()),
    path('api/v1/list/about_user/', AboutUserListApiView.as_view()),
]


