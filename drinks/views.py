from django.shortcuts import render
from drinks.models import Cocktail
# Create your views here.

def drinks(request, id):
    queryset = Cocktail.objects.filter(id=id)
    instance=queryset[0]
    cocktail_name = instance.name
    recipe = instance.recipe
    all_ingredients = instance.ingredients.all()
    ingredients = list()
    for x in range(0, len(all_ingredients)):
        ingredients.append(str(all_ingredients[x]))
    
    context_dictionary={
    "id":id,
    'cocktail_name': cocktail_name,
    'recipe': recipe,
    'instance': instance,
    'ingredients': ingredients
    }
    return render(request, 'drink.html', context_dictionary)