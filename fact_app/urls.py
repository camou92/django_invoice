from django.urls import path

from fact_app import views

urlpatterns = [
    path('', views.home, name='home')
]