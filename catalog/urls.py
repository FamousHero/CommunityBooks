from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog", views.catalog, name="catalog"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("api/wishlist", views.wishlistEndpoint, name="wishlist-endpoint"),
    path("wishlist-form", views.addWishlistForm, name="wishlist-form"),
    path("addBook", views.addBook, name="loan-form"),
    path("signup", views.signup, name="signup")
]