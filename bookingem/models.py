from django.db import models
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):

    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey(Books,
                                on_delete=models.CASCADE,
                             related_name="comment")

    def __str__(self):
        return f"{self.text}"

