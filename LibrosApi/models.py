from django.db import models

class Libro(models.Model):

    title=models.CharField(max_length=100)
    numero_de_paginas=models.IntegerField()
    dia_de_publicacion=models.DateField()
    cantidad=models.IntegerField()

    def __str__(self):
        return self.title



