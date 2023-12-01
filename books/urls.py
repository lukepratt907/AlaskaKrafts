from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("login/", views.login_page, name="login-page"),
    path("register/", views.register_page, name="register-page"),
    path("logout/", views.logout_view, name="logout-view"),
    path("about/", views.about_page, name="about-page"),
    path("favorites/", views.favorites_page, name="favorites-page"),
    path("favorite/", views.favorite_view, name="favorite-view"),
    path("cart/", views.cart_page, name="cart-page"),
    path("addtocart/", views.cart_view, name="cart-view"),
    
]