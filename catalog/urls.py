from django.urls import path

from .views import (index,
                    PositionListView,
                    WorkerListView,
                    TaskListView)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
]

app_name = "catalog"
