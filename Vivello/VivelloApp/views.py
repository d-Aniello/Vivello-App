from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView
from VivelloApp.forms import FarmForm, FieldForm, TaskForm
from VivelloApp.models import Farm, Field, VehicleType, Vehicle, MachineType, Machine, Crop, Task


class Index(View):
    """Returns home page"""

    def get(self, request):
        return render(request, 'index.html')


class CreateFarmView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Generates site with a form to create new farm"""

    permission_required = ['VivelloApp.add_farm']

    def get(self, request):
        form = FarmForm()
        return render(request, 'new_farm.html', {'form': form})

    def post(self, request):
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farms')
        return render(request, 'new_farm.html', {'form': form})


class FarmsView(LoginRequiredMixin, View):
    """List of farms in database"""

    def get(self, request):
        farms = Farm.objects.all()
        return render(request, 'farms.html', {'farms': farms})


class FarmDetailView(LoginRequiredMixin, DetailView):
    """Details of the farm"""
    model = Farm
    template_name = 'farm_detail_view.html'


class FarmDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen farm"""

    permission_required = ['VivelloApp.delete_farm']
    model = Farm
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('farms')


class CreateFieldView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Generates site with a form to create new field"""

    permission_required = ['VivelloApp.add_field']

    def get(self, request):
        form = FieldForm()
        return render(request, 'new_field.html', {'form': form})

    def post(self, request):
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fields')
        return render(request, 'new_field.html', {'form': form})


class FieldsView(LoginRequiredMixin, View):
    """List of fields in database"""

    def get(self, request):
        fields = Field.objects.all()
        return render(request, 'fields.html', {'fields': fields})


class FieldDetailView(LoginRequiredMixin, DetailView):
    """Details of the field"""
    model = Field
    template_name = 'field_detail_view.html'


class FieldDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen field"""

    permission_required = ['VivelloApp.delete_field']
    model = Field
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('fields')


class CreateVehicleTypeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Generates site with a form to create new vehicle type"""

    permission_required = ['VivelloApp.add_vehicletype']
    model = VehicleType
    fields = '__all__'
    template_name = 'new_vehicle_type.html'
    success_url = reverse_lazy('vehicle_types')


class VehicleTypesView(LoginRequiredMixin, View):
    """List of vehicle types in database"""

    def get(self, request):
        vehicle_types = VehicleType.objects.all()
        return render(request, 'vehicle_types.html', {'vehicle_types': vehicle_types})


class VehicleTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen vehicle type"""

    permission_required = ['VivelloApp.delete_vehicletype']
    model = VehicleType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicle_types')


class CreateVehicleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Generates site with a form to create new vehicle"""

    permission_required = ['VivelloApp.add_vehicle']

    def get(self, request):
        vehicle_types = VehicleType.objects.all()
        return render(request, 'new_vehicle.html', {'vehicle_types': vehicle_types})

    def post(self, request):
        name = request.POST.get('name')
        vehicle_type_id = request.POST.get('vehicle_type_id')
        vehicle_type = VehicleType.objects.get(id=vehicle_type_id)
        Vehicle.objects.create(name=name, vehicle_type=vehicle_type)
        return redirect('vehicles')


class VehiclesView(LoginRequiredMixin, View):
    """List of vehicles in database"""

    def get(self, request):
        vehicles = Vehicle.objects.all()
        return render(request, 'vehicles.html', {'vehicles': vehicles})


class VehicleDetailView(LoginRequiredMixin, DetailView):
    """Details of the vehicle"""
    model = Vehicle
    template_name = 'vehicle_detail_view.html'


class VehicleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen vehicle"""

    permission_required = ['VivelloApp.delete_vehicle']
    model = Vehicle
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('vehicles')


class CreateMachineTypeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Generates site with a form to create new machine type"""

    permission_required = ['VivelloApp.add_machinetype']
    model = MachineType
    fields = '__all__'
    template_name = 'new_machine_type.html'
    success_url = reverse_lazy('machine_types')


class MachineTypesView(LoginRequiredMixin, View):
    """List of machine types in database"""

    def get(self, request):
        machine_types = MachineType.objects.all()
        return render(request, 'machine_types.html', {'machine_types': machine_types})


class MachineTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen machine type"""

    permission_required = ['VivelloApp.delete_machinetype']
    model = MachineType
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machine_types')


class CreateMachineView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Generates site with a form to create new machine"""

    permission_required = ['VivelloApp.add_machine']

    def get(self, request):
        machine_types = MachineType.objects.all()
        return render(request, 'new_machine.html', {'machine_types': machine_types})

    def post(self, request):
        name = request.POST.get('name')
        machine_type_id = request.POST.get('machine_type_id')
        machine_type = MachineType.objects.get(id=machine_type_id)
        Machine.objects.create(name=name, machine_type=machine_type)
        return redirect('machines')


class MachinesView(LoginRequiredMixin, View):
    """List of machines in database"""

    def get(self, request):
        machines = Machine.objects.all()
        return render(request, 'machines.html', {'machines': machines})


class MachineDetailView(LoginRequiredMixin, DetailView):
    """Details of the machine"""
    model = Machine
    template_name = 'machine_detail_view.html'


class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen machine"""

    permission_required = ['VivelloApp.delete_machine']
    model = Machine
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('machines')


class CreateCropView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Generates site with a form to create new crop"""

    permission_required = ['VivelloApp.add_crop']
    model = Crop
    fields = '__all__'
    template_name = 'new_crop.html'
    success_url = reverse_lazy('crops')


class CropsView(LoginRequiredMixin, View):
    """List of crops in database"""

    def get(self, request):
        crops = Crop.objects.all()
        return render(request, 'crops.html', {'crops': crops})


class CropDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen crop"""

    permission_required = ['VivelloApp.delete_crop']
    model = Crop
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('crops')


class CreateTaskView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Generates site with a form to create new task"""

    permission_required = ['VivelloApp.add_task']

    def get(self, request):
        form = TaskForm()
        return render(request, 'new_task.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        return render(request, 'new_task.html', {'form': form})


class TasksView(LoginRequiredMixin, View):
    """List of tasks in database"""

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})


class TaskDetailView(LoginRequiredMixin, DetailView):
    """Details of the task"""
    model = Task
    template_name = 'task_detail_view.html'


class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Deletes chosen task"""

    permission_required = ['VivelloApp.delete_task']
    model = Task
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('tasks')
