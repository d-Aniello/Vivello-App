import pytest
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from VivelloApp.models import Farm, Field, VehicleType, Vehicle, MachineType, Machine, Crop, Task


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_farm_view(client, user):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_farm')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Stawiguda',
        'address': 'Olsztyn'
    }
    url = reverse('add_farm')
    response = client.post(url, dct)
    assert Farm.objects.get(**dct)


@pytest.mark.django_db
def test_farms_view(client, user):
    client.force_login(user)
    url = reverse('farms')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_farm_detail_view(client, farm, user):
    client.force_login(user)
    url = reverse('farm_detail_view', args=(farm.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_farm_delete_view(client, user, farm):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_farm')
    user.user_permissions.add(perm)
    url = reverse('farm_delete_view', args=(farm.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_field_view(client, user, farm):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_field')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Stawiguda',
        'area': 10,
        'location': 'Zadupie',
        'farm': farm.id
    }
    url = reverse('add_field')
    response = client.post(url, dct)
    assert Field.objects.get(**dct)


@pytest.mark.django_db
def test_fields_view(client, user):
    client.force_login(user)
    url = reverse('fields')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_field_detail_view(client, field, user):
    client.force_login(user)
    url = reverse('field_detail_view', args=(field.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_field_delete_view(client, user, field):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_field')
    user.user_permissions.add(perm)
    url = reverse('field_delete_view', args=(field.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_vehicle_type_view(client, user):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_vehicletype')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Ciągnik rolniczy'
    }
    url = reverse('add_vehicle_type')
    response = client.post(url, dct)
    assert VehicleType.objects.get(**dct)


@pytest.mark.django_db
def test_vehicle_types_view(client, user):
    client.force_login(user)
    url = reverse('vehicle_types')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_type_delete_view(client, user, vehicle_type):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_vehicletype')
    user.user_permissions.add(perm)
    url = reverse('vehicle_type_delete_view', args=(vehicle_type.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_vehicle_view(client, user, vehicle_type):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_vehicle')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Fendt',
        'vehicle_type': vehicle_type.id
    }
    url = reverse('add_vehicle')
    response = client.post(url, dct)
    assert Vehicle.objects.get(**dct)


@pytest.mark.django_db
def test_vehicles_view(client, user):
    client.force_login(user)
    url = reverse('vehicles')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_detail_view(client, vehicle, user):
    client.force_login(user)
    url = reverse('vehicle_detail_view', args=(vehicle.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vehicle_delete_view(client, user, vehicle):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_vehicle')
    user.user_permissions.add(perm)
    url = reverse('vehicle_delete_view', args=(vehicle.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_machine_type_view(client, user):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_machinetype')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Pług'
    }
    url = reverse('add_machine_type')
    response = client.post(url, dct)
    assert MachineType.objects.get(**dct)


@pytest.mark.django_db
def test_machine_types_view(client, user):
    client.force_login(user)
    url = reverse('machine_types')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_machine_type_delete_view(client, user, machine_type):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_machinetype')
    user.user_permissions.add(perm)
    url = reverse('machine_type_delete_view', args=(machine_type.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_machine_view(client, user, machine_type):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_machine')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Lemken',
        'machine_type': machine_type.id
    }
    url = reverse('add_machine')
    response = client.post(url, dct)
    assert Machine.objects.get(**dct)


@pytest.mark.django_db
def test_machines_view(client, user):
    client.force_login(user)
    url = reverse('machines')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_machine_detail_view(client, machine, user):
    client.force_login(user)
    url = reverse('machine_detail_view', args=(machine.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_machine_delete_view(client, user, machine):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_machine')
    user.user_permissions.add(perm)
    url = reverse('machine_delete_view', args=(machine.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_crop_view(client, user):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_crop')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Wyka',
        'variety': 'Hanka'
    }
    url = reverse('add_crop')
    response = client.post(url, dct)
    assert Crop.objects.get(**dct)


@pytest.mark.django_db
def test_crops_view(client, user):
    client.force_login(user)
    url = reverse('crops')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_crop_delete_view(client, user, crop):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_crop')
    user.user_permissions.add(perm)
    url = reverse('crop_delete_view', args=(crop.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_task_view(client, user):
    client.force_login(user)
    perm = Permission.objects.get(codename='add_task')
    user.user_permissions.add(perm)
    dct = {
        'name': 'Siew',
        'description': 'Bla bla bla',
        'date': '2022-04-02'
    }
    url = reverse('add_task')
    response = client.post(url, dct)
    assert Task.objects.get(**dct)


@pytest.mark.django_db
def test_tasks_view(client, user):
    client.force_login(user)
    url = reverse('tasks')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_task_detail_view(client, task, user):
    client.force_login(user)
    url = reverse('task_detail_view', args=(task.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_task_delete_view(client, user, task):
    client.force_login(user)
    perm = Permission.objects.get(codename='delete_task')
    user.user_permissions.add(perm)
    url = reverse('task_delete_view', args=(task.id, ))
    response = client.post(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_login_view(client, user):
    url = reverse('login')
    dct = {
        'username': 'Daniel',
        'password': 'Dupa123456'
    }
    response = client.post(url, dct)
    assert response.status_code == 302
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_logout_view(client, user):
    url = reverse('logout')
    client.force_login(user)
    response = client.get(url)
    assert response.wsgi_request.user.is_authenticated == False


@pytest.mark.django_db
def test_registration_view(client):
    url = reverse('registration')
    dct = {
        'username': 'Daniel',
        'pass_1': 'Dupa123456',
        'pass_2': 'Dupa123456'
    }
    response = client.post(url, dct)
    assert User.objects.get(**dct)


@pytest.mark.django_db
def test_user_permission_view(client, user):
    url = reverse('perm', args=(user.id, ))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_users_view(client):
    url = reverse('users')
    response = client.get(url)
    assert response.status_code == 200
