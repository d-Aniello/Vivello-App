from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView

from VivelloApp.models import Farm, Field, VehicleType, Vehicle, MachineType, Machine


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


class CreateMachineTypeView(CreateView):
    model = MachineType
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('machine_types')


class MachineTypesView(View):
    def get(self, request):
        machine_types = MachineType.objects.all()
        return render(request, 'machine_types.html', {'machine_types': machine_types})


class MachineTypeDeleteView(DeleteView):
    model = MachineType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machine_types')


class CreateMachineView(CreateView):
    model = Machine
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('machines')


class MachinesView(View):
    def get(self, request):
        machines = Machine.objects.all()
        return render(request, 'machines.html', {'machines': machines})


class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machine_detail_view.html'


class MachineDeleteView(DeleteView):
    model = Machine
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machines')
