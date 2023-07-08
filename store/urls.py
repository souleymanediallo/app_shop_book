from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('cart/<str:slug>/add-to-cart', views.add_to_cart, name='add_to_cart'),
    ]