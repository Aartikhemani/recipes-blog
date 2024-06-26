from rest_framework.routers import DefaultRouter

from recipes_manager import views
from nutrition_facts.views import IngredientViewSet

app_name = 'recipes-manager'

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'recipes', views.RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'ingredients-recipes', views.IngredientRecipeViewSet, basename='ingredients-recipes')
