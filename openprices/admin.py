from django.contrib import admin
from django import forms
from .models import products, store, ticket

class productsAdminForm(forms.ModelForm):

    class Meta:
        model = products
        fields = '__all__'


class productsAdmin(admin.ModelAdmin):
    form = productsAdminForm
    list_display = ['name_on_ticket', 'price', 'ean13', 'last_updated', 'reduction', 'store', 'quantity', 'currency']
    readonly_fields = ['name_on_ticket', 'price', 'ean13', 'last_updated', 'reduction', 'store', 'quantity', 'currency']

admin.site.register(products, productsAdmin)


class storeAdminForm(forms.ModelForm):

    class Meta:
        model = store
        fields = '__all__'


class storeAdmin(admin.ModelAdmin):
    form = storeAdminForm
    list_display = ['name', 'address', 'telephone', 'last_updated']
    readonly_fields = ['name', 'address', 'telephone', 'last_updated']

admin.site.register(store, storeAdmin)


class ticketAdminForm(forms.ModelForm):

    class Meta:
        model = ticket
        fields = '__all__'


class ticketAdmin(admin.ModelAdmin):
    form = ticketAdminForm
    list_display = ['date', 'printing_date', 'store', 'last_updated', 'image', 'image_ocr']
    readonly_fields = ['date', 'printing_date', 'store', 'last_updated', 'image', 'image_ocr']

admin.site.register(ticket, ticketAdmin)


