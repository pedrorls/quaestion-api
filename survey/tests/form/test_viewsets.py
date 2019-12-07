from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy

from ...models import Form

User = get_user_model()


class FormTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="test")
        self.user1.set_password("password")
        self.user1.save()

        self.user2 = User.objects.create_user("test2")
        self.user2.set_password("password")
        self.user2.save()

        self.form1 = mommy.make(Form, creator=self.user1)
        self.form2 = mommy.make(Form, creator=self.user1)
        self.form3 = mommy.make(Form, creator=self.user2)

    def test_get_forms(self):
        self.client.login(username="test", password="password")
        url = reverse("api:form-list")
        response = self.client.get(url, {"username": "test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_forms_as_different_user(self):
        self.client.login(username="test2", password="password")
        url = reverse("api:form-list")
        response = self.client.get(url, {"username": "test2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_cannot_see_other_users_form(self):
        self.client.login(username="test", password="password")
        url = reverse("api:form-detail", kwargs={"pk": self.form3.id})
        response = self.client.get(url, {"username": "test"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_create_form(self):
        self.client.login(username="test", password="password")
        data = {
            "title": "Test Form",
            "description": "Test description",
            "creator": self.user1.id,
        }
        response = self.client.post(reverse("api:form-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(reverse("api:form-list"), {"username": "test"})
        self.assertEqual(len(response.data), 3)

