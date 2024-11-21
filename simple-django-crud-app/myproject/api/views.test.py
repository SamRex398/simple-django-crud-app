from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

class CreateUserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_returns_201_status_with_valid_data(self):
        valid_data = {
            "name": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com"
        }
        response = self.client.post('/api/users/', valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Token.objects.count(), 1)