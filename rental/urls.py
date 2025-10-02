"""
URL configuration for car_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
   path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path('profile/', views.profile, name='profile'),
        path("jwt-login/", views.jwt_login, name="jwt_login"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path("search/", views.car_detail_list, name="search_cars"),
   
   path('cars/', views.car_list, name='car_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
   path('cars/<str:car_type>/', views.car_list, name='car_list_by_type'),
   path('search/',views.search_view,name='search'),
   
   path('service/',views.service,name='service'),
    path('cars/<int:car_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
   path('cart/',views.view_cart,name='cart'),
   path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
   path("promocode/",views.promocode,name='promocode'),

   path("checkout/",views.checkout,name='checkout'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),  

   path("order_history/", views.order_history, name="order_history"),
   path("wishlist/", views.wishlist, name="wishlist"),
    path('wishlist/add/<int:car_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:car_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
   path("luxury/",views.luxer,name='luxury'),
   path("aeroplane_detail/",views.aeroplane,name="aeroplane_detail"),

  
    
  
]

