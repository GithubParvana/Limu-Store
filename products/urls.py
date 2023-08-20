from django.urls import path
from products import views


urlpatterns = [
    # path('sale/', views.sale, name='sale'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('your-wishlist/', views.wishlists, name='wishlists'),
    path('product-list/', views.product_list, name='product_list'),



]
