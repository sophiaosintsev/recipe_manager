from django.contrib import admin
from .models import ShoppingList


class ShoppingListAdmin(admin.ModelAdmin):
    pass
admin.site.register(ShoppingList, ShoppingListAdmin)