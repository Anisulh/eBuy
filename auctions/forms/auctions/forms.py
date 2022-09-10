
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, NumberInput, Select, FileInput
from auctions.models import Bid, Comments, ListingItem

class CreateListing(ModelForm):
    class Meta:
        model = ListingItem
        exclude = ['sold', 'lister']
        labels = {
          'item_name': _('Item Name'),
          'description': _('Description'),
          'base_price': _('Starting Price'),
          'category': _('Category'),
          'images': _('Upload Images')
        }
        widgets = {
          'item_name': TextInput(attrs={'class': 'form-control w-75 p-3'}),
          'description': TextInput(attrs={'class': 'form-control w-75 p-3'}),
          'base_price': NumberInput(attrs={'class': 'form-control w-75 p-3'}),
          'category': Select(attrs={'class': 'form-select w-75'}),
          
        }

class AddComment(ModelForm):
    class Meta:
        model = Comments
        exclude= ["user", "item_name", "up_votes"]
        labels = {
          "comment": _("Comment")
        }
        widgets = {
          "comment": TextInput(attrs={'class': 'form-control w75 p-3'})
        }

class AddBid(ModelForm):
    class Meta:
      model = Bid
      exclude= ["bidder", "listing_item"]
      labels = {
          "bidding_price": _("Place Bid")
        }
      widgets = {
          "bidding_price": NumberInput(attrs={'class': 'form-control w75 p-3'})
        }