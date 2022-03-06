from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView

from VivelloApp.models import Farm, Field, VehicleType, Vehicle


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class CreateFarmView(CreateView):
    model = Farm
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('farms')


class FarmsView(View):
    def get(self, request):
        farms = Farm.objects.all()
        return render(request, 'farms.html', {'farms': farms})


class FarmDetailView(DetailView):
    model = Farm
    template_name = 'farm_detail_view.html'


class FarmDeleteView(DeleteView):
    model = Farm
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('farms')


class CreateFieldView(CreateView):
    model = Field
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('fields')


class FieldsView(View):
    def get(self, request):
        fields = Field.objects.all()
        return render(request, 'fields.html', {'fields': fields})


class FieldDetailView(DetailView):
    model = Field
    template_name = 'field_detail_view.html'


class FieldDeleteView(DeleteView):
    model = Field
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('fields')


class CreateVehicleTypeView(CreateView):
    model = VehicleType
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('vehicle_types')


class VehicleTypesView(View):
    def get(self, request):
        vehicle_types = VehicleType.objects.all()
        return render(request, 'vehicle_types.html', {'vehicle_types': vehicle_types})


class VehicleTypeDeleteView(DeleteView):
    model = VehicleType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicle_types')


class CreateVehicleView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('vehicles')


class VehiclesView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, 'vehicles.html', {'vehicles': vehicles})


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail_view.html'


class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicles')
