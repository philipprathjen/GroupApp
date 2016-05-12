from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from drinks.models import Cocktail

class IngForm(forms.Form):
	ing1 = forms.CharField(label='', required = False)
	ing2 = forms.CharField(label='', required = False)
	ing3 = forms.CharField(label='', required = False)
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Submit', 'Submit', css_class="btn btn-block btn-primary" ))

