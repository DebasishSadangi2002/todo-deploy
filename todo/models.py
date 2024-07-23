from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    compleated = models.BooleanField(default=False)

    def __str__(self):
        return self.title
