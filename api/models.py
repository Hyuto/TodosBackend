from django.db import models
from account.models import Account


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title