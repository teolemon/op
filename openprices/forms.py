from django import forms
from .models import products, store, ticket


class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['name_on_ticket', 'price', 'ean13', 'reduction', 'store', 'quantity', 'currency', 'ticket', 'user']


class storeForm(forms.ModelForm):
    class Meta:
        model = store
        fields = ['name', 'address', 'telephone']


class ticketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['date', 'printing_date', 'store', 'image', 'image_ocr', 'store', 'user']


