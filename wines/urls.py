from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('add/', views.add_wine, name='add_wine'),
    path('edit/<product_id>/', views.edit_wine, name='edit_wine'),
    path('delete/<product_id>/', views.delete_wine, name='delete_wine'),
    path('add_region/', views.add_region, name='add_region'),
    path('add_cheese/', views.add_cheese, name='add_cheese'),
    path('regions/', views.regions, name='regions'),
    path('cheeses/', views.cheeses, name='cheeses'),
]
