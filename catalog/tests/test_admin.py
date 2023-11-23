from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from catalog.models import Position, Worker, TaskType, Task


class AdminTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin_user',
            password='admin_password',
        )

        self.client = Client()
        self.client.login(username='admin_user', password='admin_password')

        self.position = Position.objects.create(name="Test Position")
        self.worker = Worker.objects.create(username="test_user", position=self.position)
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.task = Task.objects.create(
            name="Test Task",
            deadline="2023-01-01",
            is_completed=False,
            priority=Task.Priority.HIGH,
            task_type=self.task_type
        )

    def test_worker_admin(self):
        response = self.client.get('/admin/catalog/worker/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Position')

    def test_task_admin(self):
        response = self.client.get('/admin/catalog/task/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Deadline')
        self.assertContains(response, 'Is completed')
        self.assertContains(response, 'Priority')
