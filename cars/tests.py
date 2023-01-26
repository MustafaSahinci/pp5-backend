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


class CarDetailViewTests(APITestCase):
    def setUp(self):
        bozkurt = User.objects.create_user(username='bozkurt', password='pass')
        osman = User.objects.create_user(username='osman', password='pass')
        Car.objects.create(
            owner=bozkurt, title='a title', content='bozkurts content'
        )
        Car.objects.create(
            owner=osman, title='another title', content='osmans content'
        )

    def test_can_retrieve_car_using_valid_id(self):
        response = self.client.get('/cars/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_car_using_invalid_id(self):
        response = self.client.get('/cars/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_car(self):
        self.client.login(username='bozkurt', password='pass')
        response = self.client.put('/cars/1/', {'title': 'a new title'})
        car = Car.objects.filter(pk=1).first()
        self.assertEqual(car.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_car(self):
        self.client.login(username='bozkurt', password='pass')
        response = self.client.put('/cars/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
