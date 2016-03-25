# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Categoria(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nome

class Tutorial(models.Model):
	id = models.AutoField(primary_key=True)
	titulo= models.CharField(max_length=300)
	texto= models.TextField()
	criado= models.DateTimeField()
	categoria= models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.titulo

class Duvida(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=100)
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.titulo		

