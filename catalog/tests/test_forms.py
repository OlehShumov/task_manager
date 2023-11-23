from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.forms import (WorkerSearchForm,
                           PositionSearchForm,
                           TaskSearchForm,
                           TaskForm,
                           TaskUpdateForm,
                           WorkerCreationForm,
                           WorkerUpdateForm)
from catalog.models import Task, Position, TaskType


class FormsTest(TestCase):
    def setUp(self):
        position = Position.objects.create(name="Test Position")
        user = get_user_model().objects.create_user(username="test_user", password="test_password", position=position)

    def test_worker_search_form(self):
        form_data = {"username": "test_user"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_search_form(self):
        form_data = {"name": "Test Position"}
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_search_form(self):
        form_data = {"name": "Test Task"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form(self):
        form_data = {
            "name": "Test Task",
            "description": "Test Description",
            "deadline": "2023-01-01",
            "is_completed": False,
            "priority": Task.Priority.HIGH,
            "task_type": TaskType.objects.create(name="Test Type").id,
            "assignees": [get_user_model().objects.first().id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_update_form(self):
        form_data = {
            "name": "Updated Task",
            "description": "Updated Description",
            "deadline": "2023-02-01",
            "is_completed": True,
            "priority": Task.Priority.MEDIUM,
            "task_type": TaskType.objects.create(name="Updated Type").id,
            "assignees": [get_user_model().objects.first().id],
        }
        task = Task.objects.create(name="Test Task", deadline="2023-01-01", is_completed=False)
        form = TaskUpdateForm(data=form_data, instance=task)
        self.assertTrue(form.is_valid())

    def test_worker_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "new_password",
            "password2": "new_password",
            "position": Position.objects.first().id,
            "first_name": "New",
            "last_name": "User",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_update_form(self):
        form_data = {
            "username": "updated_user",
            "first_name": "Updated",
            "last_name": "User",
            "position": Position.objects.first().id,
        }
        worker = get_user_model().objects.create_user(username="test_user1", password="test_password")
        form = WorkerUpdateForm(data=form_data, instance=worker)
        self.assertTrue(form.is_valid())
