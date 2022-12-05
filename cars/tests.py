from django.contrib.auth.models import User
from .models import Car
from rest_framework import status
from rest_framework.test import APITestCase


class CarListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bozkurt', password='pass')

    def test_can_list_cars(self):
        bozkurt = User.objects.get(username='bozkurt')
        Car.objects.create(owner=bozkurt, title='a title')
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_car(self):
        self.client.login(username='bozkurt', password='pass')
        response = self.client.post('/cars/', {'title': 'a title'})
        count = Car.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_car(self):
        response = self.client.post('/cars/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)