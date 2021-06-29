from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title