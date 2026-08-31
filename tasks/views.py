from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import ProjectForm, TaskCreateForm, TaskUpdateForm
from tasks.models import Project, Task


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).prefetch_related("tasks")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_create_form"] = TaskCreateForm()
        return context


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("tasks:project-list")
    http_method_names = ["post"]

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
    form_class = TaskCreateForm

    def form_valid(self, form):
        project = get_object_or_404(
            Project,
            pk=self.kwargs["project_id"],
            owner=self.request.user,
        )
        form.instance.project = project
        task = form.save()

        return render(self.request,"tasks/partials/task.html", {"task": task})


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "tasks/partials/task_update_form.html"

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)

    def form_valid(self, form):
        task = form.save()
        return render(self.request,"tasks/partials/task.html", {"task": task})


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse("")


class TaskToggleCompleteView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, project__owner=request.user)
        task.is_completed = not task.is_completed
        task.save()

        return render(request, "tasks/partials/task.html",{"task": task})
