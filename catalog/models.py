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
    position = models.ForeignKey(Position,
                                 on_delete=models.CASCADE,
                                 related_name="workers",
                                 null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.get_full_name()}, username: {self.username}, position: {self.position}"


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = "H", "high-priority"
        MEDIUM = "M", "medium-priority"
        LOW = "L", "low-priority"
        NO = "N", "no-priority"
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=15,
                                choices=Priority.choices,
                                default=Priority.NO)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return (
            f"Task: {self.name}, "
            f"status: {'Done' if self.is_completed else 'In work'}, "
            f"priority: {self.priority}"
        )
