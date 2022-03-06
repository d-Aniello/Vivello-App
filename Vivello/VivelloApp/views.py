from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from VivelloApp.models import Farm


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class CreateFarmView(CreateView):
    model = Farm
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('add_farm')
