
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.id}: {self.name}"

class ListingItem(models.Model):
    item_name = models.CharField(max_length=128)
    description = models.TextField(default="")
    base_auction_price = models.IntegerField(blank=True)
    auction_time_limit= models.DurationField(blank=True)
    selling_price = models.IntegerField(blank=True)
    lister = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='listing_image/')
    sold = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}: name:{self.item_name} base: ${self.base_auction_price}, lister: {self.lister}, category: {self.category}"
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    up_votes = models.IntegerField(blank=True)
    item_name = models.ForeignKey(ListingItem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} said: '{self.comment}' with {self.up_votes} on this item: {self.item_name}"
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.ForeignKey(ListingItem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} is watching {self.item_name}"

class Bid(models.Model):
    listing_item = models.ForeignKey(ListingItem, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bidding_price = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: item:{self.listing_item}, bidder:{self.bidder}, bidding price:{self.bidding_price} category"

# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     street_address = models.TextField()
#     street_address2: models.TextField(blank=True)
#     city = models.TextField()
#     state = models.TextField()
#     zipcode = models.IntegerField(max_length=10)
    