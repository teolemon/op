import models
import serializers
from rest_framework import viewsets, permissions


class productsViewSet(viewsets.ModelViewSet):
    """ViewSet for the products class"""

    queryset = models.products.objects.all()
    serializer_class = serializers.productsSerializer
    permission_classes = [permissions.IsAuthenticated]


class storeViewSet(viewsets.ModelViewSet):
    """ViewSet for the store class"""

    queryset = models.store.objects.all()
    serializer_class = serializers.storeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ticketViewSet(viewsets.ModelViewSet):
    """ViewSet for the ticket class"""

    queryset = models.ticket.objects.all()
    serializer_class = serializers.ticketSerializer
    permission_classes = [permissions.IsAuthenticated]


