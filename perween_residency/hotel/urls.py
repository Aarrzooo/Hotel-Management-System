from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms, name='rooms'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path("login/", views.customer_login, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
