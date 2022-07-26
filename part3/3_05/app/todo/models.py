import uuid
from django.db import models


class Todo(models.Model):
    """Todo item model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=140)

    def __str__(self):
        return self.title
