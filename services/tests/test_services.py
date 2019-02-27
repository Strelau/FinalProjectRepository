import pytest
from django.test import Client


@pytest.mark.django_db
def test_login():
    from django.contrib.auth.models import User
    client = Client()
    User.objects.create_user(
        username='test',
        email='test1@example.com',
        password='test',
    )
    try_login  = client.post('/accounts/login/', data={
        'username': 'test',
        'password': 'test',
    })
    assert try_login.status_code == 302
