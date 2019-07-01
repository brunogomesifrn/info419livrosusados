from django.shortcuts import render, redirect
from .models import Livro, Generos
from .forms import LivroForm, GenerosForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):	
	livros = Livro.objects.all()
	contexto = {
		'livro_lista': livros
	}
	return render(request, 'index.html', contexto)

def livros(request, id):
	usuario = User.objects.get(pk=id)
	livros = Livro.objects.filter(criador=usuario)
	contexto = {
		'livro_lista': livros
	}
	return render(request, 'livros.html', contexto)

def cadLiv(request):
	form = LivroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		livro = form.save(commit=False)
		livro.criador = request.user
		livro.save()
		for genero in form.cleaned_data['generos']:
			livro.generos.add(genero)
		return redirect('index')
	contexto = {
		'form': form
	}
	return render(request, 'cadLiv.html', contexto)

def generos(request, id):	
	usuario = User.objects.get(pk=id)
	generos = Generos.objects.filter(criador=usuario)
	contexto = {
		'lista_generos': generos
	}
	return render(request, 'generos.html', contexto)

def cadGen(request):
	form = GenerosForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		generos = form.save(commit=False)
		generos.criador = request.user
		generos.save()
		return redirect('generos', generos.criador.id)
	contexto = {
		'form': form
	}
	return render(request, 'cadGen.html', contexto)

def editar(request, id):
	user = User.objects.get(pk=id)

	form = UserCreationForm(request.POST or None, instance=user)

	if form.is_valid():
		form.save()
		return redirect('index')

	contexto = {
		'form': form
	}
	return render(request, 'registration/registro.html', contexto)

def excluir(request, id):
	livro = Livro.objects.get(pk=id)
	livro.delete()
	return redirect('index')

def excluirGen(request, id):
	generos = Generos.objects.get(pk=id)
	generos.delete()
	return redirect('generos', generos.criador.id)

def login(request):
	return render(request, 'login.html')

def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'registration/registro.html', contexto)

def dados(request, id):
	user = User.objects.get(pk=id)

	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
	'form': form
	}
	return render(request, 'registration/registro.html', contexto)