# loja/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.nome


    def save(self, *args, **kwargs):
        # Verifica se a quantidade é zero ou menos
        if self.quantidade <= 0:
            self.disponivel = False
        else:
            self.disponivel = True
        
        # Chama o método save() original para salvar o objeto no banco de dados
        super().save(*args, **kwargs)