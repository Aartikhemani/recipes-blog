from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cooking_time = models.IntegerField(default=0)
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', through='IngredientRecipe')
    published_date = models.DateTimeField(auto_now_add=True)


class IngredientRecipe(models.Model):
    class MeasuringUnit(models.TextChoices):
        milligram = 'mg'
        gram = 'g'
        kg = 'kg'
        milliliter = 'ml'
        liter = 'l'

    quantity = models.FloatField()
    measuring_unit = models.CharField(max_length=256, choices=MeasuringUnit)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.OneToOneField('Ingredient', on_delete=models.CASCADE)


class Ingredient(models.Model):
    title = models.CharField(max_length=256)
    nutrition_facts = models.OneToOneField('NutritionFacts', on_delete=models.CASCADE)
