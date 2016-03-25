from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def cate():
	
	return c

def index(request):
	cate=Categoria.objects.all()
	post=Tutorial.objects.all().order_by('id').reverse()
	return render(request, 'base.html', {'cate':cate, 'post':post})

def menu(request, cat):
	cate=Categoria.objects.all()
	post=Tutorial.objects.filter(categoria__nome=cat)
	return render(request, 'cate.html', {'post':post, 'cate':cate})

def duvida(request, cat):
	cate=Categoria.objects.all()
	duvida=Duvida.objects.filter(categoria__nome=cat)
	return render(request, 'duvida.html', {'duvida':duvida, 'cate':cate})

def detalhe(request, id):
	cate=Categoria.objects.all()
	detalhe= get_object_or_404(Tutorial, id=id)	
	return render(request, 'detalhe.html', {'cate':cate, 'detalhe': detalhe})		