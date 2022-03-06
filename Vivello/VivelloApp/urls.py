"""Vivello URL Configuration

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
from django.urls import path
from VivelloApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_farm/', views.CreateFarmView.as_view(), name='add_farm'),
    path('farms/', views.FarmsView.as_view(), name='farms'),
    path('farm/<int:pk>/', views.FarmDetailView.as_view(), name='farm_detail_view'),
    path('farm/delete/<int:pk>/', views.FarmDeleteView.as_view(), name='farm_delete_view'),
    path('add_field/', views.CreateFieldView.as_view(), name='add_field'),
    path('fields/', views.FieldsView.as_view(), name='fields'),
    path('field/<int:pk>/', views.FieldDetailView.as_view(), name='field_detail_view'),
    path('field/delete/<int:pk>/', views.FieldDeleteView.as_view(), name='field_delete_view'),
]