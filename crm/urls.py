from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'crm'
urlpatterns = [
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerView.as_view(), name='customer'),
    path('relationships/', views.CustomerRelationshipsView.as_view(), name='customer-relationships'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('task/<int:pk>', views.TaskView.as_view(), name='task'),
    path('feedbacks/', views.FeedbacksView.as_view(), name='feedbacks'),
    path('feedback/<int:pk>', views.FeedbackView.as_view(), name='feedback'),
    path('bills/', views.BillsView.as_view(), name='bills'),
    path('bill/<int:pk>', views.BillView.as_view(), name='bill'),
]