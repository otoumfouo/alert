"""alert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from event import views
urlpatterns = [
    path('', views.index, name='index'),
    path('event/', views.alertList, name='list'),
    path('event/dash/pie', views.dash_pie, name='dash_pie'),
    path('event/dash/line', views.dash_line, name='dash_line'),
    path('event/create/', views.AlertCreateView.as_view(), name='create'),
    path('event/<int:pk>/update/', views.AlertUpdateView.as_view(), name='update'),
]
