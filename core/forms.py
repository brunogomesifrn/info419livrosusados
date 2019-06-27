from django.forms import ModelForm
from django import forms

from .models import Livro

class LivroForm(ModelForm):
	class Meta:
		model = Livro
		fields = ['nome', 'autor', 'preco', 'imagem', 'generos']
		widgets = {
			'generos': forms.CheckboxSelectMultiple(),
		}