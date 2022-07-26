# from django.test import TestCase

# # Create your tests here.
import json
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import TodoSerializer
from .models import Todo

# class CreateTestCase(APITestCase):

#     def test_create(self):
#         data = {
#             "task_name": "test task",
#             "completed": "true"
#         }

#         response = self.client.post("/api/task-create/", data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

class ListToDo(APITestCase):

    def list_todo(self):
        response = self.client.get("/api/task-list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)