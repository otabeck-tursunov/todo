from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    guruh = models.CharField(max_length=50, blank=True)
    st_raqam = models.PositiveIntegerField()
    tel = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

class Todo(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    description = models.TextField()
    status = models.BooleanField(default=True, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


