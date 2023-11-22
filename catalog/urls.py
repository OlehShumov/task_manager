from django.urls import path

from .views import (index,
                    PositionListView,
                    WorkerListView,
                    TaskListView,
                    PositionCreateView,
                    PositionUpdateView,
                    PositionDeleteView,
                    WorkerCreateView,
                    WorkerUpdateView,
                    WorkerDeleteView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,)

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
]

app_name = "catalog"
