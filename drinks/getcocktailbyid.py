import os, sys, django
sys.path.append("/Users/philipp_rathjen/Documents/Education/Columbia_projects/AppCode/GroupApp")
os.environ["DJANGO_SETTINGS_MODULE"] = "GroupApp.settings"
django.setup()

from urllib import request
from urllib.request import urlopen
from drinks.models import Cocktail, Ingredient
import json

# url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=15112"

def get_cocktail_and_save_it(the_id_on_site):
	x = the_id_on_site
	y= str(x)
	url = 'http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=%s' %(y)

	with urlopen(url) as response:
	        outputString = response.read().decode('utf-8')
	        jsonObject = json.loads(outputString)  
	        
	drink = jsonObject["drinks"][0]
	drink_name = drink["strDrink"]
	ing1 = drink["strIngredient1"]
	ing2 = drink["strIngredient2"]
	ing3 = drink["strIngredient3"]
	ing4 = drink["strIngredient4"]
	ing5 = drink["strIngredient5"]
	ing6 = drink["strIngredient6"]
	ing7 = drink["strIngredient7"]
	ing8 = drink["strIngredient8"]
	ing9 = drink["strIngredient9"]
	ing10 = drink["strIngredient10"]
	ing11 = drink["strIngredient11"]
	ing12 = drink["strIngredient12"]
	ing13 = drink["strIngredient13"]
	ing14 = drink["strIngredient14"]
	ing15 = drink["strIngredient15"]

	ingredient_list=[ing1, ing2, ing3, ing4, ing5, ing6, ing7, ing8, ing9, ing10, ing11, ing12, ing13, ing14, ing15]
	print(ingredient_list)
	for x in range(0, len(ingredient_list)):
		try:
			ingredient_list.remove('')
		except:
			pass

	print(ingredient_list)

	print("ID: " + drink["idDrink"])
	print("Name: " + drink["strDrink"])
	print("Recipe: " + drink["strInstructions"])
	print("Ingredient1: " + drink["strIngredient1"])
	print("Ingredient2: " + drink["strIngredient2"])
	print("Ingredient3: " + drink["strIngredient3"])
	print("Ingredient4: " + drink["strIngredient4"])
	img_url = drink['strDrinkThumb']
	try:
		request.urlretrieve(img_url, "../../media/media/cocktail_images/%s.jpg" %(drink_name))
	except:
		pass

	item = Cocktail()
	item.name = drink_name
	item.recipe = drink["strInstructions"]
	if img_url:
		item.picture = "media/cocktail_images/%s.jpg" %(drink_name)
	else:
		item.picture = "media/cocktail_images/default_edit.jpg"
	item.save()

	for x in ingredient_list:
		try: 
			ing = Ingredient.objects.get(name=x)
		except:
			ing = Ingredient(name=x)
			ing.save()
		item.ingredients.add(ing)

for x in range(10000,20000):
	try:
		get_cocktail_and_save_it(x)
	except:
		pass
