from django import forms

from tasks.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "deadline", "priority"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
