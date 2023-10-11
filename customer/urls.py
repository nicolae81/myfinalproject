from django.urls import path
from customer import views

urlpatterns = [
    path('create_customer/', views.CustomerCreateView.as_view(), name='create-customer'),
]