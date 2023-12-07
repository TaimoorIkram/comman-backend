from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'hrm'
router = DefaultRouter(trailing_slash=True)

router.register('members', views.MembersView, basename='members')

urlpatterns = [
    path('home/', views.home, name='home'),
] + router.urls