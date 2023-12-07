from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("login/", views.login_page, name="login-page"),
    path("register/", views.register_page, name="register-page"),
    path("logout/", views.logout_view, name="logout-view"),
    path("about/", views.about_page, name="about-page"),
    path("favorites/", views.favorites_page, name="favorites-page"),
    path("favorite/<int:book_id>", views.favorite_view, name="favorite-view"),
    path("removefavorite/<int:book_id>", views.removefavorite_view, name="removefavorite-view"),
    path("cart/", views.cart_page, name="cart-page"),
    path("addtocart/<int:book_id>", views.cart_view, name="cart-view"),
    path("removecart/<int:book_id>", views.removecart_view, name="removecart-view"),
    path("profilepage/", views.profile_page, name="profile-page"),
    path("editpicture/", views.editpic, name="editpic"),

    
]