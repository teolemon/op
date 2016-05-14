import models

from rest_framework import serializers


class productsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.products
        fields = (
            'id', 
            'name_on_ticket', 
            'price', 
            'ean13', 
            'last_updated', 
            'reduction', 
            'store', 
            'quantity', 
            'currency', 
        )


class storeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.store
        fields = (
            'id', 
            'name', 
            'address', 
            'telephone', 
            'last_updated', 
        )


class ticketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ticket
        fields = (
            'id', 
            'date', 
            'printing_date', 
            'store', 
            'last_updated', 
            'image', 
            'image_ocr', 
        )


