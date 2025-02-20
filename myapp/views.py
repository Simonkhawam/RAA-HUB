from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Comanda, Utilizator
from .forms import ComandaForm, UtilizatorForm
from django.urls import reverse_lazy

class ComandaCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')  # Redirect to the list view after creating

    def form_valid(self, form):
        # Add any additional logic if needed
        return super().form_valid(form)

class ComandaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_list.html'
    context_object_name = 'comenzi'  # Variable name used in the template

class ComandaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')

    def form_valid(self, form):

        return super().form_valid(form)

class ComandaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_confirm_delete.html'
    success_url = reverse_lazy('comanda-list')

class UtilizatorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')

class UtilizatorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_list.html'
    context_object_name = 'utilizatori'

class UtilizatorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')

class UtilizatorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_confirm_delete.html'
    success_url = reverse_lazy('utilizator-list')
