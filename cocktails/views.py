from django.shortcuts import render
from .forms import IngForm
from profiles.forms import LikedForm, DislikedForm
from drinks.models import Cocktail, Ingredient
from profiles.models import Profile, Liked_cocktail
from django.contrib.auth import get_user_model 
from django.db import models
import random
#Getting the user from AUTH
User = get_user_model()

# Create your views here.
def home(request):
    return render(request, 'landing.html')

def main(request):
    return render(request, 'main.html')

def about_us(request):
    return render(request, 'about_us.html')


def cocktail_finder(request):
	form_ing = IngForm()
	form_liked = LikedForm()
	form_disliked = DislikedForm()
	Liked_Drinks = Liked_cocktail.objects.all()
	num = None
	Cocktails = Cocktail.objects.all()

	if request.method == 'GET':
		try:
			# Collect form responses from GET request
			ing1 = request.GET['ing1']
			ing2 = request.GET['ing2']
			ing3 = request.GET['ing3']
			# Filter the cocktails for those specified in the form
			Cocktails = Cocktail.objects.filter(ingredients__name=ing1)
			if ing2:
				Cocktails = Cocktails.filter(ingredients__name=ing2)
			if ing3:
				Cocktails = Cocktails.filter(ingredients__name=ing3)

		except:
			# You need this because you cant reference the variables in the return dictionary without
			# having defined them 
			ing1 = None
			ing2 = None
			ing3 = None
		# I create a session. And pass the form values over
		request.session['ing1'] = ing1
		request.session['ing2'] = ing2
		request.session['ing3'] = ing3
		

	elif request.method =='POST':
		# I collect the form values
		ing1 = request.session['ing1']
		ing2 = request.session['ing2']
		ing3 = request.session['ing3']
		# I apply the filtering algorithm again with the variables we passed over
		if ing1: 
			Cocktails = Cocktail.objects.filter(ingredients__name=ing1)
		if ing2:
			Cocktails = Cocktails.filter(ingredients__name=ing2)
		if ing3:
			Cocktails = Cocktails.filter(ingredients__name=ing3)
		try:
			# Collect the form data from the post request.
			# You want to save the liked/disliked information to the database
			liked = request.POST['liked']
			if liked == '0':
				liked = False
			else:
				liked = True
			user = request.POST['user']
			cocktail = request.POST['cocktail']
			print('hello world')
			print(liked, cocktail, user)
			# To save something we create an object. --> b
			if form_liked.is_valid:
				b = Liked_cocktail()
				b.liked = liked
				print(b.liked)
				b.cocktail = Cocktail.objects.get(id=cocktail)
				b.user = Profile.objects.get(id=user)
				print(b.liked)
				try:
					b.create()
				except:
					b.save()	
		except:
			pass
	else:
		ing1 = None
		ing2 = None
		ing3 = None
	
	# Filter for the cocktails that you haven't previously liked
	for d in range(0, len(Liked_Drinks)):
		if str(Liked_Drinks[d].user) == str(request.user):
			drink = str(Liked_Drinks[d].cocktail)
			Cocktails = Cocktails.exclude(name = drink)
	# once you run out of cocktails to display, redirect to landing page. 
	try: 
		Cocktails = random.choice(Cocktails)
	except: 
		return render(request, "landing.html")
	
	# Pre-populate the forms with the relevant data 
	num = Cocktails.id
	data1 = {'cocktail': num, 'user': request.user.id, 'liked': 1}
	data2 = {'cocktail': num, 'user': request.user.id, 'liked': 0}
	ingredient_request = {'ing1': ing1, 'ing2': ing2, 'ing3': ing3}
	form_liked = LikedForm(data1)
	form_disliked = DislikedForm(data2)
	form_ing = IngForm(ingredient_request)
	
	if not Cocktails:
		Cocktails=None
	else:
		all_ingredients= Cocktails.ingredients.all()
		ingredients = list()
		for x in range(0, len(all_ingredients)):
			ingredients.append(str(all_ingredients[x]))

	context_dictionary={
		'form_ing': form_ing,
		'form_liked': form_liked,
		'form_disliked': form_disliked,
		"ing1": ing1,
		"ing2": ing2,
		"ing3": ing3,
		"Cocktails": Cocktails,
		'num': num,
		'ingredients': ingredients,
	}
	return render(request, "cocktail_finder.html", context_dictionary)

