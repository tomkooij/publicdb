from django.contrib import admin

from .models import (Leverancier, Opbergplek, Artikel, Apparatuur,
                     Reservering, Gebruikt, Bestel, HisparcII)


class LeverancierAdmin(admin.ModelAdmin):
    list_display = ('naam', 'woonplaats', 'land', 'telefoon', 'contactpersoon')
    list_filter = ('woonplaats', 'land')
    search_fields = ('naam', )


class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('naam', 'opbergplek', 'aantal', 'leverancier', 'datum',
                    'commentaar')
    list_filter = ('opbergplek', 'leverancier')
    search_fields = ('naam', )


class ApparatuurAdmin(admin.ModelAdmin):
    list_display = ('naam', 'opbergplek', 'aantal')
    search_fields = ('naam', )


class ReserveringAdmin(admin.ModelAdmin):
    list_display = ('cluster', 'artikel', 'aantal', 'datum', 'voldaan')
    list_filter = ('cluster', 'voldaan')
    search_fields = ('artikel', )


class GebruiktAdmin(admin.ModelAdmin):
    list_display = ('persoon', 'artikel', 'aantal', 'datum', 'cluster')
    list_filter = ('persoon', 'cluster')


class BestelAdmin(admin.ModelAdmin):
    list_display = ('persoon', 'artikel', 'aantalbesteld', 'datumbesteld',
                    'levertijd', 'aantalgeleverd', 'datumgeleverd', 'voldaan')
    list_filter = ('persoon', 'voldaan')
    search_fields = ('artikel', )


class HisparcIIAdmin(admin.ModelAdmin):
    list_display = ('serienummer', 'is_master', 'stationnummer',
                    'opstelling', 'plaats', 'status', 'opmerkingen')


admin.site.register(Leverancier, LeverancierAdmin)
admin.site.register(Opbergplek)
admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Apparatuur, ApparatuurAdmin)
admin.site.register(Reservering, ReserveringAdmin)
admin.site.register(Gebruikt, GebruiktAdmin)
admin.site.register(Bestel, BestelAdmin)
admin.site.register(HisparcII, HisparcIIAdmin)
