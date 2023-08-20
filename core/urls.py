from django.urls import path
from core import views


urlpatterns = [
    path('about-us/', views.about, name='about'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faqs, name='faq'),
    path('404-not-found/', views.not_found, name='not-found'),

]
