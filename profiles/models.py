from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from drinks.models import Cocktail
# Create your models here.

User = settings.AUTH_USER_MODEL

def upload_location(instance, filename):
	extension = filename.split(".")[1]
	location = instance.user.username
	return '%s/profile.%s' %(location, extension)

class Profile(models.Model):
	user = models.OneToOneField(User)
		# OneToOneField any user can only have one profile. Kind of a unique clause
	picture = models.ImageField(upload_to ="media/profile_images/%s" %(upload_location), null=True, blank = True)

	def __str__(self):
		return self.user.username	

	def get_absolute_url(self):
		url = reverse('profile', kwargs={'username': self.user.username}) 
		#This actually gives us the URL
		return url

class Liked_cocktail(models.Model):
	user = models.ForeignKey(Profile)
	cocktail = models.ForeignKey(Cocktail)
	liked = models.NullBooleanField(null=True, blank=True)
