from django.db import models

class Conteudo(models.Model):
    CATEGORIA_CHOICES = [
        ('sugestoes', 'Sugestões'),
        ('formas', 'Formas'),
        ('elementos', 'Elementos'),
    ]

    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, default='')
    imagem = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='sugestoes')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo