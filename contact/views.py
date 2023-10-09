from django.core.mail import send_mail
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from contact.form import ContactForm


# Create your views here.
class ContactUsFormView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        subject = 'New contact form submission'
        message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nMessage: {form.cleaned_data["message"]}'
        send_mail(subject, message, 'your-email@example.com', ['recipient@example.com'])

        return super().form_valid(form)


