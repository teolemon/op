from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import products, store, ticket
from .forms import productsForm, storeForm, ticketForm

#class UploadTicket(TemplateView):

#class ProcessTicket(TemplateView):
#Process through Google Cloud Vision or OCR
#Store text
#Match text to existing values
#Output EAN

class productsListView(ListView):
    model = products


class productsCreateView(CreateView):
    model = products
    form_class = productsForm


class productsDetailView(DetailView):
    model = products


class productsUpdateView(UpdateView):
    model = products
    form_class = productsForm


class storeListView(ListView):
    model = store


class storeCreateView(CreateView):
    model = store
    form_class = storeForm


class storeDetailView(DetailView):
    model = store


class storeUpdateView(UpdateView):
    model = store
    form_class = storeForm


class ticketListView(ListView):
    model = ticket


class ticketCreateView(CreateView):
    model = ticket
    form_class = ticketForm


class ticketDetailView(DetailView):
    model = ticket


class ticketUpdateView(UpdateView):
    model = ticket
    form_class = ticketForm

