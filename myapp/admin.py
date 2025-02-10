from django.contrib import admin
from .models import Utilizator, Comanda, TipStatie, TipComanda, StadiulComenzii

@admin.register(TipStatie)
class TipStatieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(TipComanda)
class TipComandaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(StadiulComenzii)
class StadiulComenziiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'end_date')
    search_fields = ('name', 'status')
    list_filter = ('status',)
    ordering = ('status',)

@admin.register(Utilizator)
class UtilizatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'prenume', 'nume', 'email', 'telefon', 'tip_statie', 'department')
    search_fields = ('username', 'prenume', 'nume', 'email', 'department')
    list_filter = ('tip_statie', 'department')
    ordering = ('prenume', 'nume')

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Order Details', {
            'fields': ('order_number', 'client_name', 'agent_name', 'code_art')
        }),
        ('Dates', {
            'fields': ('start_date', 'due_date', 'end_date')
        }),
        ('Status and Type', {
            'fields': ('status', 'order_type')
        }),
    )
    list_display = ('id', 'order_number', 'client_name', 'start_date', 'due_date', 'status', 'order_type')
    search_fields = ('order_number', 'client_name', 'agent_name')
    list_filter = ('status', 'order_type', 'start_date', 'due_date')
    ordering = ('start_date',)
    date_hierarchy = 'start_date'
