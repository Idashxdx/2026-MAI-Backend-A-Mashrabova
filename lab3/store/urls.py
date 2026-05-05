from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile),
    path('products/', views.products),
    path('category/', views.category),
    path('favorite/', views.add_favorite),
]
