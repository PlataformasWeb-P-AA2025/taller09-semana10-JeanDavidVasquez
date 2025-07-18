# Generated by Django 5.2.3 on 2025-06-11 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('auspiciante', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('siglas', models.CharField(max_length=10)),
                ('twitter_username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='futbolec.campeonato')),
                ('equipo_futbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campeonatos', to='futbolec.equipofutbol')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion_campo', models.CharField(max_length=50)),
                ('numero_camiseta', models.IntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipo_futbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='futbolec.equipofutbol')),
            ],
        ),
    ]
