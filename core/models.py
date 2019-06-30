from django.db import models
from django.contrib.auth.models import User
class Generos(models.Model):
	nome = models.CharField('Nome', max_length=100)

	def __str__(self):
		return self.nome

class Livro(models.Model):
	nome = models.CharField('Nome', max_length=100)
	autor = models.CharField('Autor', max_length=100)
	preco = models.DecimalField('Preco', max_digits=5, decimal_places=2, null = True)
	imagem = models.ImageField('Imagem', upload_to='media/', max_length=100)
	generos = models.ManyToManyField(Generos)
	criador = models.ForeignKey(User, on_delete=models.CASCADE)