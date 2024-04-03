from django.db import models


class Ingredient(models.Model):
    title = models.CharField(max_length=256)
    serving_size_g = models.FloatField()
    calories = models.FloatField()
    protein_g = models.FloatField()
    suger_g = models.FloatField()
    fat_total_g = models.FloatField()
    carbohydrates_total_g = models.FloatField()
    cholesterol_mg = models.FloatField()
    potassium_mg = models.FloatField()
    sodium_mg = models.FloatField()
    fiber_g = models.FloatField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Ingredient(pk={repr(self.pk)}, title={repr(self.title)})"

    class Meta:
        ordering = ("title",)
