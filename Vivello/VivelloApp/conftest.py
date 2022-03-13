import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient

from VivelloApp.models import Farm


@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def farms():
    lst = []
    a = Farm.objects.create(name='Golub', address='Dobrzyń')
    lst.append(a)
    a = Farm.objects.create(name='PGR', address='Warszawa')
    lst.append(a)
    a = Farm.objects.create(name='Basia', address='Milicz')
    lst.append(a)
    return lst
