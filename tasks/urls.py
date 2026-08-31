from django.urls import path

from tasks.views import ProjectCreateView, ProjectDeleteView, ProjectListView, ProjectUpdateView

app_name = "tasks"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path("projects/<int:pk>/update/", ProjectUpdateView.as_view(), name="project-update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(),name="project-delete"),
]
