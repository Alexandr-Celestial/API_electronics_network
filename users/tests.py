from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(APITestCase):

    def setUp(self):
        """Создаёт тестовые данные"""

        self.email = "user@test.ru"
        self.password = "1234"

    def test_user_registration(self):
        """Тест регистрации пользователя"""

        data = {
            "email": self.email,
            "password": self.password,
        }
        response = self.client.post("/users/token/register/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="user@test.ru").exists())
