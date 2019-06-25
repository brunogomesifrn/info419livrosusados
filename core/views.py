from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):	
	livros = Livro.objects.all()
	contexto = {
		'lista_livro': livros
	}
	return render(request, 'index.html', contexto)

def cadLiv(request):
	form = LivroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect(index)
	contexto = {
		'form': form
	}
	return render(request, 'cadLiv.html', contexto)

def excluir(request, id):
	livro = Livro.objects.get(pk=id)
	livro.delete()
	return('index')

def login(request):
	return render(request, 'login,html')

@login_required
def usuario(request):
	return render(request, 'usuario.html')