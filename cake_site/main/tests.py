from django.test import TestCase, Client
from .models import Cake
from django.contrib.auth.models import User


class TestAuthentification(TestCase):

    def test_registration(self):
        form_data = {'username': "Yulia", 'password1': "12345", 'password2': "12345"}
        response = self.client.post("/registration", data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        form_data = {'username': "admiin", 'password': "12345"}
        response = self.client.post("/login", data=form_data)
        self.assertEqual(response.status_code, 200)

class CakeCreateTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='Yulia')
        user.set_password('12345')
        user.save()
        self.client.login(username="Yulia", password="12345")

    def test_cake_post_valid_form(self):
        form_data = {'name': "Красный бархат", "anons": "Супер вкусный",
                     'price': "55"}
        response = self.client.post("/create", data=form_data)
        self.assertEqual(response.status_code, 200)


    def test_dcake_post_invalid_form(self):
        form_data = {'name': "Красный бархат"}
        self.client.post("/create", data=form_data)
        self.assertFalse(Cake.objects.filter(name='Красный бархат').exists())
