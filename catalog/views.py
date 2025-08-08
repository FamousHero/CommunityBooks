# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "catalog/index.html")

def catalog(request):
    return render(request, "catalog/catalog.html")

def wishlist(request):
    return render(request, "catalog/wishlist.html")

def addBook(request):
    return render(request, "catalog/loan-form.html")

def signup(request):
    return render(request, "catalog/signup.html")

def addWishlistForm(request):
    return render(request, "catalog/wishlist-form.html")

def wishlistEndpoint(request):
    data = { 
        "books": [
            {"title": "The Girl with the Dragon Tattoo", "author": "John Doe"},
            {"title": "To Kill A Mocking Bird", "author": "Mary Jane"},
        ]
    }
    return JsonResponse(data)