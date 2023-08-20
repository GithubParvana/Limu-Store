from django.urls import path
from blogs import views


urlpatterns = [
    path('blog-list/', views.blog_list, name='blog-list'),
    path('blog-detail-left/', views.blog_detail_left, name='blog-detail-left'),
    path('blog-grid-view/', views.blog_grid_view, name='blog-grid-view'),
   
    


]
