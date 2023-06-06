from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    task = models.TextField()
    created = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Todos"