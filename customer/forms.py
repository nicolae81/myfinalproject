from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # in formularul generat in interfata se vor afisa toate

        # fieldurile din modelul Student

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'start_date': DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            # type="datetime-local"
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # type="datetime-local"
            'gender': Select(attrs={'class': 'form-select'}),

        }
