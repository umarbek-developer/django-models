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
    

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    founded_year = models.SmallIntegerField(default=0, null=True)
    owner_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} {self.address}"
    

    class Meta:
        verbose_name = "Company"
        verbose_name_plural ="Companies"
        ordering = ['company_name', 'founded_year']





class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)
    group_number = models.CharField(max_length=50)
    students_count = models.PositiveSmallIntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher} {self.universitet} {self.students_count}"




class StudentDavomat(models.Model):
    class BahoChoice(models.IntegerChoices):
        BESH = 5, "5-baho"
        TORT = 4, "4-baho"
        UCH = 3, "3-baho"
        IKKI = 2, "2-baho"
        BIR = 1, "1-baho"
        NOL = 0, "0-baho"

    class StatusChoice(models.TextChoices):
        KELDI = "keldi", "keldi"
        ONLINE = "online", "Online Qatnashdi"
        SABABLI = "sababli", "Sababli kelmagan"
        YOQ = "yoq", "Darsga kelmagan"
        

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    baho = models.IntegerField(choices=BahoChoice.choices, default=BahoChoice.NOL)
    status = models.CharField(max_length=50, choices=StatusChoice.choices, default=StatusChoice.KELDI)
    created_at = models.DateField(auto_now_add=50)

    def __str__(self):
        return f"{self.status} {self.baho}"

