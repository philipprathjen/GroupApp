from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Liked_cocktail

#### Turning liked checkbox into Button button: 


class LikedForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Submit', '', css_class="btn btn-success" ))     

	class Meta:
		model = Liked_cocktail
		fields = '__all__'
		widgets = {'user': forms.HiddenInput(), 'cocktail': forms.HiddenInput(), 'liked':forms.HiddenInput()}
		# exclude  = ('user', 'cocktail',)

class DislikedForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Submit', '', css_class="btn btn-danger" ))     

	class Meta:
		model = Liked_cocktail
		fields = '__all__'
		widgets = {'user': forms.HiddenInput(), 'cocktail': forms.HiddenInput(), 'liked':forms.HiddenInput()}
		# exclude  = ('user', 'cocktail',)
		