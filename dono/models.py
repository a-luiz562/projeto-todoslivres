from django.db import models

# Create your models here
class Dono(models.Model):
    nome = models.CharField(max_length=255)
    endereco = 'rua paraiso'
    telefone = int ('41445070')

    def __str__(self):
        return self.nome