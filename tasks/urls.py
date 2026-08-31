from django.urls import path

from tasks.views import ProjectCreateView, ProjectListView

app_name = "tasks"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create",
),
]
