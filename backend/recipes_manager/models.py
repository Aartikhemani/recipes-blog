from django.contrib.auth.models import User
from django.db import models

from nutrition_facts.models import Ingredient

from custom_user.models import CustomUser


def user_directory_path(instance, filename):
    return f"user_{instance.email}/{filename}"


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Category(pk={repr(self.pk)}, title={repr(self.title)})"

    class Meta:
        ordering = ("title",)


class Recipe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cooking_time = models.IntegerField(default=0)
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="IngredientRecipe")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Recipe(pk={repr(self.pk)}, title={repr(self.title)}), user={repr(self.user)})"

    class Meta:
        ordering = ("title",)


class IngredientRecipe(models.Model):
    class MeasuringUnit(models.TextChoices):
        milligram = "mg"
        gram = "g"
        kg = "kg"
        milliliter = "ml"
        liter = "l"

    title = models.CharField(max_length=256, default='Ingredient')
    quantity = models.FloatField()
    measuring_unit = models.CharField(
        max_length=256, choices=MeasuringUnit.choices, default=MeasuringUnit.gram
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"IngredientRecipe(pk={repr(self.pk)}, title={repr(self.title)}, quantity={repr(self.quantity)})"


