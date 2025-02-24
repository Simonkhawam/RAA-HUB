from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Comanda, Utilizator
from .forms import ComandaForm, UtilizatorForm
from django.urls import reverse_lazy

class ComandaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')
    permission_required = "myapp.add_comanda"
    raise_exception = False

    def form_valid(self, form):
        return super().form_valid(form)


class ComandaListView(LoginRequiredMixin, ListView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_list.html'
    context_object_name = 'comenzi'
    # permission_required = "myapp.view_comanda"
    # raise_exception = False
    #
    #
    # def get_queryset(self):
    #     return Comanda.objects.all().order_by('id')

class ComandaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'myapp/comanda/comanda_form.html'
    success_url = reverse_lazy('comanda-list')
    permission_required = "myapp.change_comanda"
    raise_exception = False

    def form_valid(self, form):
        return super().form_valid(form)

class ComandaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comanda
    template_name = 'myapp/comanda/comanda_confirm_delete.html'
    success_url = reverse_lazy('comanda-list')
    permission_required = "myapp.delete_comanda"
    raise_exception = True

class UtilizatorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')
    permission_required = "myapp.add_utilizator"
    raise_exception = True

class UtilizatorListView(LoginRequiredMixin, ListView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_list.html'
    context_object_name = 'utilizatori'
    # permission_required = "myapp.view_utilizator"
    # raise_exception = False

class UtilizatorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Utilizator
    form_class = UtilizatorForm
    template_name = 'myapp/utilizator/utilizator_form.html'
    success_url = reverse_lazy('utilizator-list')
    permission_required = "myapp.change_utilizator"
    raise_exception = True

class UtilizatorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Utilizator
    template_name = 'myapp/utilizator/utilizator_confirm_delete.html'
    success_url = reverse_lazy('utilizator-list')
    permission_required = "myapp.delete_utilizator"
    raise_exception = True
