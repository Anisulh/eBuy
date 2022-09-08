from django.contrib import admin
from .models import Comments, ListingItem, Bid, Categories, Watchlist

# Register your models here.
admin.site.register(ListingItem)
admin.site.register(Bid)
admin.site.register(Categories)
admin.site.register(Watchlist)
admin.site.register(Comments)