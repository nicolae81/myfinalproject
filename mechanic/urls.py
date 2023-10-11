from django.urls import path
from mechanic import views

urlpatterns = [
    path('create_mechanic/', views.MechanicCreateView.as_view(), name='create-mechanic'),
]