from django import forms

from tasks.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "deadline", "priority"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
