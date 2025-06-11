from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from futbolec.models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos


class EquipoFutbolResource(resources.ModelResource):
    class Meta:
        model = EquipoFutbol
        exclude = ('jugadores', )

class EquipoFutbolAdmin(ImportExportModelAdmin):
    resource_class = EquipoFutbolResource
    list_display = ('nombre', 'siglas', 'twitter_username')
    search_fields = ('nombre', 'siglas')
    exclude = ('jugadores',)

admin.site.register(EquipoFutbol, EquipoFutbolAdmin)

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador
        exclude = ('equipo_futbol', )

class JugadorAdmin(ImportExportModelAdmin):
    resource_class = JugadorResource
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'get_equipo_futbol')
    search_fields = ('nombre', 'equipo_futbol__nombre')

    def get_equipo_futbol(self, obj):
        return obj.equipo_futbol.nombre
    get_equipo_futbol.short_description = 'Equipo de Fútbol'

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato

class CampeonatoAdmin(ImportExportModelAdmin):
    resource_class = CampeonatoResource
    list_display = ('nombre', 'auspiciante')
    search_fields = ('nombre', 'auspiciante')

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEquiposResource(resources.ModelResource):
    class Meta:
        model = CampeonatoEquipos
        exclude = ('equipo_futbol', 'campeonato')

class CampeonatoEquiposAdmin(ImportExportModelAdmin):
    resource_class = CampeonatoEquiposResource
    list_display = ('anio', 'get_equipo_futbol', 'get_campeonato')
    search_fields = ('anio', 'equipo_futbol__nombre', 'campeonato__nombre')

    def get_equipo_futbol(self, obj):
        return obj.equipo_futbol.nombre
    get_equipo_futbol.short_description = 'Equipo de Fútbol'

    def get_campeonato(self, obj):
        return obj.campeonato.nombre
    get_campeonato.short_description = 'Campeonato'

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
