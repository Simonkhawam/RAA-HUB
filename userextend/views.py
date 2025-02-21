from unittest.mock import DEFAULT

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView
import random

from My_Final_Project.settings import DEFAULT_FROM_EMAIL
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    # fields = ['username', 'email', 'password']
    success_url = '/login/'

    # Metoda form_valid() care este o metoda folosita pt clasele de view-uri(CreateView, Update View),  iar atunci
    # cand datele din formular sunt trimise catre salvare, programatorul poate sa suplimenteze cu actiuni noi.

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_user = form.save(
    #             commit=False)  # opresc salvarea datelor in DB dar stochez obiectul in variabila new_user
    #         new_user.first_name = new_user.first_name.title()
    #         # Atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
    #         new_user.last_name = new_user.last_name.title()
    #         new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'
    #         new_user.save()  # salvez noul user
    #
    #         # trimitere mail
    #
    #         subject = 'Cont nou in aplicatie!'  # se poate scrie orice ca subiect
    #         message = f"""Felicitari {new_user.first_name} {new_user.last_name},
    #         Contul tau a fost creat cu succes!
    #
    #         Pentru autentificare te rog sa te loghezi cu username-ul: {new_user.username}
    #         """
    #         send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])
    #
    #     return redirect('login')