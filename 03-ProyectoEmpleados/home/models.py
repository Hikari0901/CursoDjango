from django.db import models
#Comandos: python manage makemigrations, python manage migrate, (estos sirven para migrar el modelo a la BD)
# Create your models here.
class Prueba(models.Model):
    #crear los atributos
    titulo= models.CharField(max_length=30)
    subtitulo= models.CharField(max_length=50)