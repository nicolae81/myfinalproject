from django.urls import path
from django.views.generic import TemplateView

from contact import views

urlpatterns = [
    path('', views.ContactUsFormView.as_view(), name='contact_form'),
    path('contact/success/', TemplateView.as_view(template_name='contact/contact_success.html'),
         name='contact_success'),
]