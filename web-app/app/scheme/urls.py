from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('relationships_terms', views.relationships_terms, name='scheme'),
    path('create', views.create),
]
