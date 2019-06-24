from django.db import models
	
class Livro(models.Model):
	nome = models.CharField('Nome', max_length=100)
	autor = models.CharField('autor', max_length=100)
	preço = models.DecimalField('preço', max_digits=5, decimal_places=2, null = True)
	
		

# Create your models here.
