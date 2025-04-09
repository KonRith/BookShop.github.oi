# Computer/urls.py
from django.urls import path, include
from . import views

app_name = 'Computer'

urlpatterns = [
# ... your existing URL patterns ...
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/update/<slug:slug>/', views.update_quantity, name='update_quantity'),
    path('cart/remove/<slug:slug>/', views.remove_item, name='remove_item'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('cart/payment/', views.payment, name='payment'),
   

    path('search/', views.search_results, name='search_results'),
    # "All" computers
    path('', views.computer_list, name='computer_list'),
    path('new-computer/', views.computer_new, name='new-computer'),

    # Brand-specific routes (must come before the generic slug)
    path('acer/', views.computer_list_Acer, name='computer_list_Acer'),
    path('acer/<slug:slug>/', views.computer_detail_Acer, name='computer_detail_Acer'),
    
    path('asus/', views.computer_list_Asus, name='computer_list_Asus'),
    path('asus/<slug:slug>/', views.computer_detail_Asus, name='computer_detail_Asus'),
    
    path('msi/', views.computer_list_Msi, name='computer_list_Msi'),
    path('msi/<slug:slug>/', views.computer_detail_Msi, name='computer_detail_Msi'),

    path('lenovo/', views.computer_list_Lenovo, name='computer_list_Lenovo'),
    path('lenovo/<slug:slug>/', views.computer_detail_Lenovo, name='computer_detail_Lenovo'),

    path('mac/', views.computer_list_Mac, name='computer_list_Mac'),
    path('mac/<slug:slug>/', views.computer_detail_Mac, name='computer_detail_Mac'),

    path('mac_a/', views.computer_list_Mac_A, name='computer_list_Mac_A'),
    path('mac_a/<slug:slug>/', views.computer_detail_Mac_A, name='computer_detail_Mac_A'),

    path('mac_b/', views.computer_list_Mac_B, name='computer_list_Mac_B'),
    path('mac_b/<slug:slug>/', views.computer_detail_Mac_B, name='computer_detail_Mac_B'),

    path('mac_c/', views.computer_list_Mac_C, name='computer_list_Mac_C'),
    path('mac_c/<slug:slug>/', views.computer_detail_Mac_C, name='computer_detail_Mac_C'),

    # Generic detail route LAST
    path('<slug:slug>/', views.computer_detail, name='computer_detail'),

]
