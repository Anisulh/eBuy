from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from auctions.forms.auctions.forms import CreateListing

from .models import Categories, ListingItem, User, Watchlist


def index(request):
    return render(request, "auctions/index.html",{
        "listings": ListingItem.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request, id):
    listing_item = ListingItem.objects.get(pk = id)
    watchlist = Watchlist.objects.filter(item_name = id).exists()
    print(watchlist)
    return render(request, "auctions/listing.html", {
        'listing_item': listing_item,
        'watchlist': watchlist
    })
    
def create_listing (request):
    if request.method == "POST":
        form = CreateListing(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                return redirect(index)
    form = CreateListing()      
    return render(request, "auctions/create_listing.html", {
        'form': form
    })
    
def profile(request):
    listing_items = ListingItem.objects.filter(lister = request.user)
    return render(request, "auctions/profile.html", {
        'listing_items': listing_items
    })

def watchlist(request):
    user = request.user
    watchlist_exists = Watchlist.objects.filter(user = user.id).exists()
    if watchlist_exists == True:
        watchlist = Watchlist.objects.filter(user = user.id)
    else:
        watchlist = False
    print(watchlist)
    return render(request, "auctions/watchlist.html", {"watchlist": watchlist})

def add_watchlist(request, id):
    user = request.user
    listing = get_object_or_404(ListingItem, id = request.POST.get('add'))
    Watchlist.objects.create(user=user, item_name = listing )
    return redirect('listing', id)
    
def remove_watchlist(request, id):
    user = request.user
    listing = get_object_or_404(ListingItem, id = request.POST.get('remove'))
    item = Watchlist.objects.get(user=user.id, item_name = listing )
    if item:
        item.delete()
    return redirect('listing', id)

    
def categories(request):
    categories = Categories.objects.all()
    return render(request, "auctions/categories.html", {"categories": categories})

def categories_listing(request, id):
    items_exists = ListingItem.objects.filter(category = id).exists()
    if items_exists == True:
        items = ListingItem.objects.filter(category = id)
    else:
        items = False

    return render(request, "auctions/category_listing.html", {
        "items": items
    })