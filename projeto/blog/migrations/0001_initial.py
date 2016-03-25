# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('categoria', models.ForeignKey(to='blog.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('criado', models.DateTimeField()),
                ('categoria', models.ForeignKey(to='blog.Categoria')),
            ],
        ),
    ]
