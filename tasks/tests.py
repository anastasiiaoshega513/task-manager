from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Project

User = get_user_model()


class ProjectAccessTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass12345")
        self.other = User.objects.create_user(username="other", password="pass12345")
        self.project = Project.objects.create(name="Owner's project", owner=self.owner)

    def test_project_list_requires_login(self):
        response = self.client.get(reverse("tasks:project-list"))
        self.assertRedirects(
            response,
            f"/accounts/login/?next={reverse('tasks:project-list')}",
        )

    def test_project_list_shows_only_own_projects(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.get(reverse("tasks:project-list"))
        self.assertNotIn(self.project, response.context["projects"])

    def test_user_cannot_delete_other_users_project(self):
        self.client.login(username="other", password="pass12345")
        response = self.client.post(reverse("tasks:project-delete", args=[self.project.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Project.objects.filter(pk=self.project.pk).exists())

    def test_owner_can_delete_own_project(self):
        self.client.login(username="owner", password="pass12345")
        response = self.client.post(reverse("tasks:project-delete", args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())
