from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone)
    # on deletion of user, their posts get deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)