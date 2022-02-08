from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'class': 'input',
                'placeholder': 'City',
                'data-form-filed': 'Name',
                'id': 'name-form1-5'
            })
        }