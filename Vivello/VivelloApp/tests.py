import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from VivelloApp.models import Farm, Field, VehicleType, Vehicle, MachineType, Machine, Crop, Task


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_farm_view(client):
    dct = {
        'name': 'Stawiguda',
        'address': 'Olsztyn'
    }
    url = reverse('add_farm')
    response = client.post(url, dct)
    assert Farm.objects.get(**dct)


@pytest.mark.django_db
def test_farms_view(client, authors):
    url = reverse('authors')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['authors'].count() == len(authors)
    for item in authors:
        assert item in context['authors']
