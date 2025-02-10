from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.
from .models import Comanda, Utilizator
from .forms import ComandaForm, UtilizatorForm
from django.urls import reverse_lazy

class ComandaCreateView(CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')  # Redirect to the list view after creating

    def form_valid(self, form):
        # Add any additional logic if needed
        return super().form_valid(form)

class ComandaListView(ListView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_list.html'
    context_object_name = 'comenzi'  # Variable name used in the template

class ComandaUpdateView(UpdateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')

    def form_valid(self, form):

        return super().form_valid(form)

class ComandaDeleteView(DeleteView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_confirm_delete.html'
    success_url = reverse_lazy('comanda-list')

class UtilizatorCreateView(CreateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')

class UtilizatorListView(ListView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_list.html'
    context_object_name = 'utilizatori'

class UtilizatorUpdateView(UpdateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')

class UtilizatorDeleteView(DeleteView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_confirm_delete.html'
    success_url = reverse_lazy('utilizator-list')
