import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient
from VivelloApp.models import Farm, Crop, Field, VehicleType, Vehicle, MachineType, Machine, Task


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


@pytest.fixture
def farm():
    b = Farm.objects.create(name='PGR', address='Wilkowyje')
    return b


@pytest.fixture
def user():
    u = User.objects.create(username='Daniel')
    u.set_password('Dupa123456')
    u.save()
    return u


@pytest.fixture
def crops():
    lst = []
    a = Crop.objects.create(name='Wyka', variety='Hanka')
    lst.append(a)
    a = Crop.objects.create(name='Bobik', variety='Bobas')
    lst.append(a)
    a = Crop.objects.create(name='Orkisz', variety='Witras')
    lst.append(a)
    return lst


@pytest.fixture
def field(farm):
    b = Field.objects.create(name='Pole', area=10, location='Zadupie', farm=farm)
    return b


@pytest.fixture
def vehicle_type():
    f = VehicleType.objects.create(name='Kombajn zbożowy')
    return f


@pytest.fixture
def vehicle(vehicle_type):
    f = Vehicle.objects.create(name='Fendt', vehicle_type=vehicle_type)
    return f


@pytest.fixture
def machine_type():
    f = MachineType.objects.create(name='Pług')
    return f


@pytest.fixture
def machine(machine_type):
    f = Machine.objects.create(name='Lemken', machine_type=machine_type)
    return f


@pytest.fixture
def crop():
    f = Crop.objects.create(name='Wyka', variety='Hanka')
    return f


@pytest.fixture
def task():
    f = Task.objects.create(name='Siew', description='Bla', date='2022-04-04')
    return f
