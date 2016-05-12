from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Liked_cocktail
from django.contrib.auth import get_user_model 


# Create your views here.
User = get_user_model()

@login_required
def profile_view(request, username):
	user = get_object_or_404(User, username=username)
	profile, created = Profile.objects.get_or_create(user=user)
	liked = Liked_cocktail.objects.filter(liked="2")
	liked = liked.filter(user=profile)
	# liked = liked.values_list('cocktail', flat=True).distinct()
	print(type(liked))
	print(liked)
	context = {
		'profile': profile,
		'liked': liked
				}

	return render(request, 'profiles/profile.html', context)