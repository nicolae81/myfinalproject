from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactUsFormView.as_view(), name='contact_form'),

]
