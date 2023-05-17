from django.contrib import admin
from .models import *

class FormulaBaseColorInline(admin.TabularInline):
    model = Formule_Base_Couleur


class ColorFormulaAdmin(admin.ModelAdmin):
    inlines = [FormulaBaseColorInline]
# Register your models here.
admin.site.register(marque)
admin.site.register(voiture)
admin.site.register(couleur,ColorFormulaAdmin)
admin.site.register(Base_Couleur)
admin.site.register(Formule_Base_Couleur)

