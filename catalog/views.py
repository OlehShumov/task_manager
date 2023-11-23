from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import (Position,
                     Worker,
                     Task)


def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
    }

    return render(request, "catalog/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "catalog/position_list.html"
    paginate_by = 5


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "catalog/worker_list.html"
    paginate_by = 5


class TaskListView(generic.ListView):
    model = Worker
    queryset = Task.objects.all().select_related("task_type").prefetch_related("assignees__tasks")
    context_object_name = "task_list"
    template_name = "catalog/task_list.html"
    paginate_by = 5



class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("catalog:position-list")


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("catalog:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("catalog:position-list")


class WorkerCreateView(generic.CreateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("catalog:worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("catalog:worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")
