from django.forms import ModelForm
from django import forms

from .models import Livro, Generos

class LivroForm(ModelForm):
	class Meta:
		model = Livro
		fields = ['nome', 'autor', 'preco', 'imagem', 'generos']
		widgets = {
			'generos': forms.CheckboxSelectMultiple(),
		}

class GenerosForm(ModelForm):
	class Meta:
		model = Generos
		fields = ['nome']