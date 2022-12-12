from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Recipe(models.Model):
    """
    Recipe model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.TextField()
    method = models.TextField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
