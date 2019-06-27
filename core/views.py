from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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

def generos(request):	
	livros = Livro.objects.all()
	contexto = {
		'lista_livro': livros
	}
	return render(request, 'generos.html', contexto)

def cadGen(request):
	form = LivroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect(index)
	contexto = {
		'form': form
	}
	return render(request, 'cadGen.html', contexto)

def excluir(request, id):
	livro = Livro.objects.get(pk=id)
	livro.delete()
	return('index')

def login(request):
	return render(request, 'login.html')

@login_required
def perfil(request):
	return render(request, 'perfil.html')


def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'registro.html', contexto)

def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
	'form': form
	}
	return render(request, 'registro.html', contexto)