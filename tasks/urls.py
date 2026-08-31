from django.urls import path

from tasks.views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectListView,
    ProjectUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskToggleCompleteView,
    TaskUpdateView,
)

app_name = "tasks"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"),
    path(
        "projects/<int:project_id>/tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/toggle-complete/",
        TaskToggleCompleteView.as_view(),
        name="task-toggle-complete",
    ),
]
