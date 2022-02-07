from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # no parenthesis means we aren't executing the function at that time
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # User has one to many relationship with Post

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
