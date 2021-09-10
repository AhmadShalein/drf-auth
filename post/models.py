from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post.detail',args=(self.id) ,kwargs={'pk': self.pk})