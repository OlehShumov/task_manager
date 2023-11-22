from django.shortcuts import render
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
    context_object_name = "task_list"
    template_name = "catalog/task_list.html"
    paginate_by = 5
