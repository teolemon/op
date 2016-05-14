import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import products, store, ticket
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_products(**kwargs):
    defaults = {}
    defaults["name_on_ticket"] = "name_on_ticket"
    defaults["price"] = "price"
    defaults["ean13"] = "ean13"
    defaults["reduction"] = "reduction"
    defaults["store"] = "store"
    defaults["quantity"] = "quantity"
    defaults["currency"] = "currency"
    defaults.update(**kwargs)
    if "ticket" not in defaults:
        defaults["ticket"] = create_ticket()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return products.objects.create(**defaults)


def create_store(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["address"] = "address"
    defaults["telephone"] = "telephone"
    defaults.update(**kwargs)
    return store.objects.create(**defaults)


def create_ticket(**kwargs):
    defaults = {}
    defaults["date"] = "date"
    defaults["printing_date"] = "printing_date"
    defaults["store"] = "store"
    defaults["image"] = "image"
    defaults.update(**kwargs)
    if "store" not in defaults:
        defaults["store"] = create_store()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return ticket.objects.create(**defaults)


class productsViewTest(unittest.TestCase):
    '''
    Tests for products
    '''
    def setUp(self):
        self.client = Client()

    def test_list_products(self):
        url = reverse('openprices_products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_products(self):
        url = reverse('openprices_products_create')
        data = {
            "name_on_ticket": "name_on_ticket",
            "price": "price",
            "ean13": "ean13",
            "reduction": "reduction",
            "store": "store",
            "quantity": "quantity",
            "currency": "currency",
            "ticket": create_ticket().id,
            "user": create_django.contrib.auth.models.user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_products(self):
        products = create_products()
        url = reverse('openprices_products_detail', args=[products.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_products(self):
        products = create_products()
        data = {
            "name_on_ticket": "name_on_ticket",
            "price": "price",
            "ean13": "ean13",
            "reduction": "reduction",
            "store": "store",
            "quantity": "quantity",
            "currency": "currency",
            "ticket": create_ticket().id,
            "user": create_django.contrib.auth.models.user().id,
        }
        url = reverse('openprices_products_update', args=[products.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class storeViewTest(unittest.TestCase):
    '''
    Tests for store
    '''
    def setUp(self):
        self.client = Client()

    def test_list_store(self):
        url = reverse('openprices_store_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_store(self):
        url = reverse('openprices_store_create')
        data = {
            "name": "name",
            "address": "address",
            "telephone": "telephone",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_store(self):
        store = create_store()
        url = reverse('openprices_store_detail', args=[store.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_store(self):
        store = create_store()
        data = {
            "name": "name",
            "address": "address",
            "telephone": "telephone",
        }
        url = reverse('openprices_store_update', args=[store.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ticketViewTest(unittest.TestCase):
    '''
    Tests for ticket
    '''
    def setUp(self):
        self.client = Client()

    def test_list_ticket(self):
        url = reverse('openprices_ticket_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_ticket(self):
        url = reverse('openprices_ticket_create')
        data = {
            "date": "date",
            "printing_date": "printing_date",
            "store": "store",
            "image": "image",
            "store": create_store().id,
            "user": create_django.contrib.auth.models.user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_ticket(self):
        ticket = create_ticket()
        url = reverse('openprices_ticket_detail', args=[ticket.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_ticket(self):
        ticket = create_ticket()
        data = {
            "date": "date",
            "printing_date": "printing_date",
            "store": "store",
            "image": "image",
            "store": create_store().id,
            "user": create_django.contrib.auth.models.user().id,
        }
        url = reverse('openprices_ticket_update', args=[ticket.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


