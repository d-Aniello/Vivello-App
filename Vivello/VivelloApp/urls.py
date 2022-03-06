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
    path('add_farm/', views.CreateFarmView.as_view(), name='add_farm'),
    path('farms/', views.FarmsView.as_view(), name='farms'),
    path('farm/<int:pk>/', views.FarmDetailView.as_view(), name='farm_detail_view'),
    path('farm/delete/<int:pk>/', views.FarmDeleteView.as_view(), name='farm_delete_view'),
    path('add_field/', views.CreateFieldView.as_view(), name='add_field'),
    path('fields/', views.FieldsView.as_view(), name='fields'),
    path('field/<int:pk>/', views.FieldDetailView.as_view(), name='field_detail_view'),
    path('field/delete/<int:pk>/', views.FieldDeleteView.as_view(), name='field_delete_view'),
    path('add_vehicle_type/', views.CreateVehicleTypeView.as_view(), name='add_vehicle_type'),
    path('vehicle_types/', views.VehicleTypesView.as_view(), name='vehicle_types'),
    path('vehicle_type/delete/<int:pk>/', views.VehicleTypeDeleteView.as_view(), name='vehicle_type_delete_view'),
    path('add_vehicle/', views.CreateVehicleView.as_view(), name='add_vehicle'),
    path('vehicles/', views.VehiclesView.as_view(), name='vehicles'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail_view'),
    path('vehicle/delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='vehicle_delete_view'),
    path('add_machine_type/', views.CreateMachineTypeView.as_view(), name='add_machine_type'),
    path('machine_types/', views.MachineTypesView.as_view(), name='machine_types'),
    path('machine_type/delete/<int:pk>/', views.MachineTypeDeleteView.as_view(), name='machine_type_delete_view'),
    path('add_machine/', views.CreateMachineView.as_view(), name='add_machine'),
    path('machines/', views.MachinesView.as_view(), name='machines'),
    path('machine/<int:pk>/', views.MachineDetailView.as_view(), name='machine_detail_view'),
    path('machine/delete/<int:pk>/', views.MachineDeleteView.as_view(), name='machine_delete_view'),
    path('add_crop/', views.CreateCropView.as_view(), name='add_crop'),
    path('crops/', views.CropsView.as_view(), name='crops'),
    path('crop/delete/<int:pk>/', views.CropDeleteView.as_view(), name='crop_delete_view'),
]