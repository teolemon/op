from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'products', api.productsViewSet)
router.register(r'store', api.storeViewSet)
router.register(r'ticket', api.ticketViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for products
    url(r'^openprices/products/$', views.productsListView.as_view(), name='openprices_products_list'),
    url(r'^openprices/products/create/$', views.productsCreateView.as_view(), name='openprices_products_create'),
    url(r'^openprices/products/detail/(?P<id>\S+)/$', views.productsDetailView.as_view(), name='openprices_products_detail'),
    url(r'^openprices/products/update/(?P<id>\S+)/$', views.productsUpdateView.as_view(), name='openprices_products_update'),
)

urlpatterns += patterns('',
    # urls for store
    url(r'^openprices/store/$', views.storeListView.as_view(), name='openprices_store_list'),
    url(r'^openprices/store/create/$', views.storeCreateView.as_view(), name='openprices_store_create'),
    url(r'^openprices/store/detail/(?P<id>\S+)/$', views.storeDetailView.as_view(), name='openprices_store_detail'),
    url(r'^openprices/store/update/(?P<id>\S+)/$', views.storeUpdateView.as_view(), name='openprices_store_update'),
)

urlpatterns += patterns('',
    # urls for ticket
    url(r'^openprices/ticket/$', views.ticketListView.as_view(), name='openprices_ticket_list'),
    url(r'^openprices/ticket/create/$', views.ticketCreateView.as_view(), name='openprices_ticket_create'),
    url(r'^openprices/ticket/detail/(?P<id>\S+)/$', views.ticketDetailView.as_view(), name='openprices_ticket_detail'),
    url(r'^openprices/ticket/update/(?P<id>\S+)/$', views.ticketUpdateView.as_view(), name='openprices_ticket_update'),
)

