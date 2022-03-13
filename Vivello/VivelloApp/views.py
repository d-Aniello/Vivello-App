from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView
from VivelloApp.models import Farm, Field, VehicleType, Vehicle, MachineType, Machine, Crop, Task


class Index(View):
    """Returns home page"""
    def get(self, request):
        return render(request, 'index.html')


class CreateFarmView(CreateView):
    """Generates site with a form to create new farm"""
    model = Farm
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('farms')


class FarmsView(View):
    """List of farms in database"""
    def get(self, request):
        farms = Farm.objects.all()
        return render(request, 'farms.html', {'farms': farms})


class FarmDetailView(DetailView):
    """Details of the farm"""
    model = Farm
    template_name = 'farm_detail_view.html'


class FarmDeleteView(DeleteView):
    """Deletes chosen farm"""
    model = Farm
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('farms')


class CreateFieldView(CreateView):
    """Generates site with a form to create new field"""
    model = Field
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('fields')


class FieldsView(View):
    """List of fields in database"""
    def get(self, request):
        fields = Field.objects.all()
        return render(request, 'fields.html', {'fields': fields})


class FieldDetailView(DetailView):
    """Details of the field"""
    model = Field
    template_name = 'field_detail_view.html'


class FieldDeleteView(DeleteView):
    """Deletes chosen field"""
    model = Field
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('fields')


class CreateVehicleTypeView(CreateView):
    """Generates site with a form to create new vehicle type"""
    model = VehicleType
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('vehicle_types')


class VehicleTypesView(View):
    """List of vehicle types in database"""
    def get(self, request):
        vehicle_types = VehicleType.objects.all()
        return render(request, 'vehicle_types.html', {'vehicle_types': vehicle_types})


class VehicleTypeDeleteView(DeleteView):
    """Deletes chosen vehicle type"""
    model = VehicleType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicle_types')


class CreateVehicleView(CreateView):
    """Generates site with a form to create new vehicle"""
    model = Vehicle
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('vehicles')


class VehiclesView(View):
    """List of vehicles in database"""
    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, 'vehicles.html', {'vehicles': vehicles})


class VehicleDetailView(DetailView):
    """Details of the vehicle"""
    model = Vehicle
    template_name = 'vehicle_detail_view.html'


class VehicleDeleteView(DeleteView):
    """Deletes chosen vehicle"""
    model = Vehicle
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicles')


class CreateMachineTypeView(CreateView):
    """Generates site with a form to create new machine type"""
    model = MachineType
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('machine_types')


class MachineTypesView(View):
    """List of machine types in database"""
    def get(self, request):
        machine_types = MachineType.objects.all()
        return render(request, 'machine_types.html', {'machine_types': machine_types})


class MachineTypeDeleteView(DeleteView):
    """Deletes chosen machine type"""
    model = MachineType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machine_types')


class CreateMachineView(CreateView):
    """Generates site with a form to create new machine"""
    model = Machine
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('machines')


class MachinesView(View):
    """List of machines in database"""
    def get(self, request):
        machines = Machine.objects.all()
        return render(request, 'machines.html', {'machines': machines})


class MachineDetailView(DetailView):
    """Details of the machine"""
    model = Machine
    template_name = 'machine_detail_view.html'


class MachineDeleteView(DeleteView):
    """Deletes chosen machine"""
    model = Machine
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machines')


class CreateCropView(CreateView):
    """Generates site with a form to create new crop"""
    model = Crop
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('crops')


class CropsView(View):
    """List of crops in database"""
    def get(self, request):
        crops = Crop.objects.all()
        return render(request, 'crops.html', {'crops': crops})


class CropDeleteView(DeleteView):
    """Deletes chosen crop"""
    model = Crop
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('crops')


class CreateTaskView(CreateView):
    """Generates site with a form to create new task"""
    model = Task
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('tasks')


class TasksView(View):
    """List of tasks in database"""
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})


class TaskDetailView(DetailView):
    """Details of the task"""
    model = Task
    template_name = 'task_detail_view.html'


class TaskDeleteView(DeleteView):
    """Deletes chosen task"""
    model = Task
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('tasks')
