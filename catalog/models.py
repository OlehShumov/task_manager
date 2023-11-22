from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return self.position


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    PRIORITY_CHOICES = [
        (0, 'high-priority'),
        (1, 'medium-priority'),
        (2, 'low-priority'),
        (3, 'no-priority'),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return (
            f"{self.name} - Assignees: "
            f"{', '.join(worker.username for worker in self.assignees.all())}"
        )
