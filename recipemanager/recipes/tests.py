from django.test import TestCase
from django import forms

from .forms import AddRecipeForm
from .models import Recipe


class TestAddRecipeForm(TestCase):

    def test_add_recipe_on_save(self):
        self.assertEqual(Recipe.objects.count(), 0)
        form = AddRecipeForm(self.data)
        form.save()

        self.assertEqual(Recipe.objects.count(), 1)

