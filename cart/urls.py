from django.urls import path
from cart import views


urlpatterns = [
    path('shop/', views.shop_page, name='shop'),
    # path('cart/', views.cart_page, name='cart'),
    path('cart/', views.shop_cart_page, name='cart'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('compare/', views.compare_page, name='compare'),
    # path('shop-left-sidebar/', views.shop_left_sidebar_page, name='shop-left-sidebar'),
    
]