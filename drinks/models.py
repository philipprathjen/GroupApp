from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.



class Ingredient(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Cocktail(models.Model):
	name = models.CharField(max_length=250)
	ingredients = models.ManyToManyField(Ingredient)
	recipe = models.TextField(default='No Recipe')
	picture = models.ImageField(upload_to ='media/cocktail_images', null=True, blank = True)
	def __str__(self):
		return self.name	

	def get_absolute_url(self):
		return "/posts/%s" %(self.id)



