from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, NumberInput, Select
from auctions.models import Categories, ListingItem

class CreateListing(ModelForm):
    class Meta:
        model = ListingItem
        exclude = ['sold']
        labels = {
          'item_name': _('Item Name'),
          'description': _('Description'),
          'base_price': _('Starting Price'),
          'category': _('Category'),
        }
        widgets = {
          'item_name': TextInput(attrs={'class': 'form-control w-75 p-3'}),
          'description': TextInput(attrs={'class': 'form-control w-75 p-3'}),
          'base_price': NumberInput(attrs={'class': 'form-control w-75 p-3'}),
          'category': Select(attrs={'class': 'form-control w-75 p-3'}),
          'lister': Select(attrs={'class': 'form-control w-75 p-3'}),
        }
