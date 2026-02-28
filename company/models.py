from django.db import models
from darslik.models import Student, Teacher, Universitet
from salom.models import Avto
from zor.models import BuTestModel

# Create your models here.
class Company(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    unversitet = models.ManyToManyField(Universitet, blank=True)
    avto = models.OneToOneField(Avto, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    butestmodel = models.ForeignKey(BuTestModel, on_delete=models.CASCADE)