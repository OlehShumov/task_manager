from django.test import TestCase
from django.utils import timezone
from catalog.models import Task, TaskType, Position, Worker


class TaskModelTest(TestCase):
    def setUp(self):
        task_type = TaskType.objects.create(name="Test Task Type")
        position = Position.objects.create(name="Test Position")
        worker = Worker.objects.create(username="test_user", position=position)
        deadline = timezone.now().date()

        self.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            deadline=deadline,
            is_completed=False,
            priority=Task.Priority.HIGH,
            task_type=task_type,
        )
        self.task.assignees.add(worker)

    def test_task_str_method(self):
        self.assertEqual(
            str(self.task), "Task: Test Task, status: In work, priority: H"
        )

    def test_task_priority_choices(self):
        task = Task.objects.create(
            name="Test Task 2",
            description="Test Description 2",
            deadline=timezone.now().date(),
            is_completed=False,
            priority=Task.Priority.LOW,
        )
        self.assertEqual(task.priority, Task.Priority.LOW)
