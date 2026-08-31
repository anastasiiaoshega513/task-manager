from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import ProjectForm, TaskForm
from tasks.models import Project, Task


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).prefetch_related("tasks")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasks:project-list")

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:project-list")

    def form_valid(self, form):
        project = get_object_or_404(
            Project,
            pk=self.kwargs["project_id"],
            owner=self.request.user,
        )
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:project-list")

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:project-list")

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)


class TaskToggleCompleteView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__owner=request.user)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("tasks:project-list")
