from django.db import models

# Create your models here.

### Crear las siguientes entidades:


#* Equipo de Futbol: nombre, siglas, username twitter

#* Jugador: nombre, posición campo, número camiseta, sueldo, equipo de fútbol

#* Campeonato: nombre de campeonato, nombre de auspiciante

#* Campeonato Equipos: año, equipo de fútbol, campeonato

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    twitter_username = models.CharField(max_length=50)

    def __str__(self):
         return "%s - %s - %s" % (self.nombre, self.siglas, self.twitter_username)
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - numero_camiseta: %d - Sueldo: %.2f - Equipo: %s" % (self.nombre, self.posicion_campo, self.numero_camiseta, self.sueldo, self.equipo_futbol.nombre)
    
class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.nombre, self.auspiciante)
    
class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    equipo_futbol = models.ForeignKey(EquipoFutbol, related_name='campeonatos', on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='equipos', on_delete=models.CASCADE)

    def __str__(self):
        return "Año: %d - Equipo: %s - Campeonato: %s" % (self.anio, self.equipo_futbol.nombre, self.campeonato.nombre)