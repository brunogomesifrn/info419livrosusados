from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm
# Create your views here.
def index(request):	
	return render(request, 'index.html')

def cadLiv(request):
	form = LivroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect(Livro)
	contexto = {
	'form': form
	}
	return render(request, 'cadLiv.html', contexto)