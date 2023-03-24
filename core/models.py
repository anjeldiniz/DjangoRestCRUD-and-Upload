from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.id}'
    
class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")

    def __str__(self):
        return self.title