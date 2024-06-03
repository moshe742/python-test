from django.test import (
    TestCase,
)

from rest_framework.test import APITestCase

from .models import Task


# Create your tests here.
class AccountTestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Test', description='this is a test task')
        # self.task.save()

    def test_get_all_tasks(self):
        res = self.client.get('/tasks/')
        expected = [{'id': self.task.id, 'title': 'Test', 'description': 'this is a test task', 'status': False}]
        actual = res.json()
        self.assertEqual(expected, actual)

    def test_get_task_by_id(self):
        res = self.client.get(f'/tasks/{self.task.id}/')
        expected = {'id': self.task.id, 'title': 'Test', 'description': 'this is a test task', 'status': False}
        actual = res.json()
        self.assertEqual(expected, actual)

    def test_create_task(self):
        res = self.client.post('/tasks/', {'title': 'Test 2', 'description': 'this is a test task 2'})
        actual = res.json()
        expected = {'id': actual['id'], 'title': 'Test 2', 'description': 'this is a test task 2', 'status': False}
        self.assertEqual(expected, actual)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        res = self.client.put(f'/tasks/{self.task.id}/', {'title': 'Test', 'description': 'this is a test task', 'status': True})
        expected = {'id': self.task.id, 'title': 'Test', 'description': 'this is a test task', 'status': True}
        actual = res.json()
        self.assertEqual(expected, actual)

    def test_delete_task(self):
        res = self.client.delete(f'/tasks/{self.task.id}/')
        self.assertEqual(Task.objects.count(), 0)

    def test_invalid_data(self):
        invalid_task_name = 'a' * 250
        res = self.client.post('/tasks/', {'title': invalid_task_name, 'description': 'this is a test'})
        expected = {'title': ['Ensure this field has no more than 200 characters.']}
        actual = res.json()
        self.assertEqual(expected, actual)

    def test_non_existing_task(self):
        res = self.client.get('/tasks/3/')
        expected = {'detail': 'No Task matches the given query.'}
        actual = res.json()
        self.assertEqual(expected, actual)
