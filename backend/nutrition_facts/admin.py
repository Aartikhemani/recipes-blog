from django.contrib import admin

from .models import NutritionFacts


@admin.register(NutritionFacts)
class NutritionFactsAdmin(admin.ModelAdmin):
    pass
