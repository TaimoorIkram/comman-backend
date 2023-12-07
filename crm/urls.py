from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'crm'
urlpatterns = [
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerView.as_view(), name='customer'),
    path('relationships/', views.CustomerRelationshipsView.as_view(), name='customer-relationships'),
]