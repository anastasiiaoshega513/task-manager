from django import forms

from tasks.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "_": "on load focus() me",
                }
            ),
        }


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Start typing here to create a task..."}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "deadline", "priority"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
