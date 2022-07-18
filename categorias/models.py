from django.db import models


class Categoria(models.Model):
    nome_categ = models.CharField(max_length=45)


    def __str__(self):
        return self.nome_categ
    