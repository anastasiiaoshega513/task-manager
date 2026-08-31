from django.conf import settings
from django.db import models


class Priority(models.IntegerChoices):
    LOW = 1, "Low"
    MEDIUM = 2, "Medium"
    HIGH = 3, "High"
    URGENT = 4, "Urgent"


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=Priority, default=Priority.LOW)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    def __str__(self):
        return self.name
