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
    success_url = '/login/'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(
                commit=False)  # opresc salvarea datelor in DB dar stochez obiectul in variabila new_user
            new_user.first_name = new_user.first_name.title()
            # Atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.last_name = new_user.last_name.title()
            new_user.save()  # salvez noul user

            # trimitere mail

            subject = 'Noul tau cont!'  # se poate scrie orice ca subiect
            message = f"""Felicitari {new_user.first_name}, Contul tau a fost creat cu succes!
            Pentru autentificare te rog sa te loghezi cu link-ulo de mai jos: 
            https://raahub-16a5dd72bf90.herokuapp.com/login/
            
            Bun venit in echipa RAA! 
            """
            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])

        return redirect('login')