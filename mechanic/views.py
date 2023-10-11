from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mechanic.forms import MechanicForm
from mechanic.models import Mechanic



class MechanicCreateView(CreateView):
    template_name = 'mechanic/create_mechanic.html'
    model = Mechanic
    form_class = MechanicForm
    success_url = reverse_lazy('home_page')
    success_message = 'Mecanicul {fname} {lname} a fost adaugat cu success.Adresa lui/ei de email este {email}'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(fname=self.object.first_name, lname=self.object.last_name,
                                           email=self.object.email)
