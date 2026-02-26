from django.db import models


class Universitet(models.Model):
    nom = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    students_count = models.SmallIntegerField(default=0)
    director_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='university-images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom}, {self.students_count}"



    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitetlar"
        ordering = ['created_at', 'nom']



class Teacher(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    experience_year = models.PositiveSmallIntegerField(default=0)
    salary = models.PositiveBigIntegerField(default=0)
    groups_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.salary}"




class Student(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    gpa = models.FloatField(default = 0)
    age = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.age}"
    


