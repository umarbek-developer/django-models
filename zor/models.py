from django.db import models
from darslik.models import Student

# Create your models here.

class BuTestModel(models.Model):
    test_nom = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey("darslik.Teacher", on_delete=models.CASCADE)

    def str(self):
        return f"{self.test_nom}"