from django.core.urlresolvers import reverse
from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class products(models.Model):

    # Fields
    name_on_ticket = models.CharField(max_length=1255)
    price = models.TextField(max_length=255)
    ean13 = models.TextField(max_length=1255)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    reduction = models.TextField(max_length=300)
    store = models.TextField(max_length=1200)
    quantity = models.TextField(max_length=100)
    currency = models.TextField(max_length=600)

    # Relationship Fields
    ticket = models.ForeignKey('openprices.ticket', )
    user = models.ForeignKey(User, )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('openprices_products_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('openprices_products_update', args=(self.id,))


class store(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    address = models.CharField()
    telephone = models.CharField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('openprices_store_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('openprices_store_update', args=(self.id,))


class ticket(models.Model):

    # Fields
    date = models.DateTimeField(max_length=255)
    printing_date = models.DateTimeField()
    store = models.CharField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    image = models.TextField()
    image_ocr = models.TextField()

    # Relationship Fields
    store = models.ForeignKey('openprices.store', )
    user = models.ForeignKey(User, )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('openprices_ticket_detail', args=(self.id,))


    def get_update_url(self):
        return reverse('openprices_ticket_update', args=(self.id,))


