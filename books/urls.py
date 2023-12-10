from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import forms
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
    path("contact/", views.contact_page, name="contact-page"),
    path("search/", views.search_books, name="search-books"),
    path("checkout/", views.checkout_page, name="checkout-page"),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]