from django.db import models

# Create your models here.
class Brend(models.Model):
    nom = models.CharField(max_length=255)
    yaratuvchi_ism = models.CharField(max_length=255)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    

class Avto(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()


