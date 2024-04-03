from rest_framework import serializers
from .models import Recipe, Category, IngredientRecipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientRecipe
        fields = "__all__"
