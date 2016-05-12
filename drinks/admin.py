from django.contrib import admin

# Register your models here.

# Change display in Admin

from .models import Cocktail, Ingredient

admin.site.register(Cocktail)
admin.site.register(Ingredient)
