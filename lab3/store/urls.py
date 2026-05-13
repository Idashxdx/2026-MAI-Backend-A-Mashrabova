from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile),

    path('products/', views.products),
    path('products/<int:watch_id>/', views.watch_detail),

    path('category/', views.category),
    path('category/<int:category_id>/', views.category_detail),

    path('favorite/', views.add_favorite),

    path('search/', views.search),
    path('watches/', views.watches),
    path('watches/create/', views.create_watch),
]
