from django.test import TestCase, Client
from .models import Cake
from django.contrib.auth.models import User


class TestAuthentification(TestCase):

    def test_registration(self):
        form_data = {'username': "Nina", 'password1': "qwer05350113", 'password2': "qwer05350113"}
        response = self.client.post("/Register", data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        form_data = {'username': "Ngd", 'password': "qwer"}
        response = self.client.post("/login", data=form_data)
        self.assertEqual(response.status_code, 200)

class CakeCreateTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='Anna')
        user.set_password('1234')
        user.save()
        self.client.login(username="Anna", password="1234")

    def test_cake_post_valid_form(self):
        form_data = {'name': "fish", "anons": "fish from russia",
                     'price': "i don't know"}
        response = self.client.post("/create", data=form_data)
        self.assertEqual(response.status_code, 200)


    def test_dcake_post_invalid_form(self):
        form_data = {'name': "fish"}
        self.client.post("/create", data=form_data)
        self.assertFalse(Cake.objects.filter(nameofdishes='fish').exists())