from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from customer.forms import CustomerForm
from customer.models import History
from customer.models import Customer


# Create your views here.
class CustomerCreateView(CreateView):
    template_name = "customer/create_customer.html"
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy(
        'customer')  # dupa salvarea datelor in tabela specificam unde sa fie redirectionat utilizatorul
    success_message = ('Clientul/a {fname} {lname} a fost adaugat cu success. '
                       'Adresa lui/ei de email este {email}')
    permission_required = 'client.add_client'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(fname=self.object.first_name,
                                           lname=self.object.last_name,
                                           email=self.object.email)

    def form_valid(self, form):
        if form.is_valid():
            new_customer = form.save()
            history_text = f'{new_customer.first_name} {new_customer.last_name} was successfuly created on {datetime.now()}'
            History.objects.create(text=history_text, created_at=datetime.now(), active=True, user=self.request.user)
        return redirect('home_page')
