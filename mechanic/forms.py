from django import forms
from django.forms import TextInput, EmailInput, Select

from mechanic.models import Mechanic


class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            # 'course': Select(attrs={'class': 'form-control', 'placeholder': 'Please enter your expertise', 'rows': 3}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'specialization': Select(attrs={'class': 'form-select'}),
        }

