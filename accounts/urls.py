from django.urls import path
from accounts import views


urlpatterns = [
    path('account/', views.login_register_page, name='login_register_page'),
    path('profile/', views.profiles, name='profiles'),
    
    
]
