from django.urls import path
from .views import (index, gaming_build_detail, laptop_detail, armchair_detail, mice_detail, keyboard_detail,
                    monitor_detail, user_login, register, all_products, filter_by_category, cart, to_cart)

urlpatterns = [
    path('', index, name='index'),
    path('gaming_detail/<int:gaming_id>/', gaming_build_detail, name='gaming_build_detail'),
    path('laptop_detail/<int:laptop_id>/', laptop_detail, name='laptop_detail'),
    path('armchair_detail/<int:armchair_id>/', armchair_detail, name='armchair_detail'),
    path('mice_detail/<int:mice_id>/', mice_detail, name='mice_detail'),
    path('keyboard_detail/<int:keyboard_id>/', keyboard_detail, name='keyboard_detail'),
    path('monitor_detail/<int:monitor_id>/', monitor_detail, name='monitor_detail'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('all_products/', all_products, name='all_products'),
    path('filter_by_category/<int:category_id>/', filter_by_category, name='filter_by_category'),
    path('cart/', cart, name='cart'),
    path('to-cart/<int:gaming_id>/<str:action>/', to_cart, name='to_cart')
]
