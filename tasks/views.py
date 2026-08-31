from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from tasks.models import Project


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).prefetch_related("tasks")
