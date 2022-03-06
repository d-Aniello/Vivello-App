from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView

from VivelloApp.models import Farm


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


class BookDeleteView(DeleteView):
    model = Farm
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('farms')
