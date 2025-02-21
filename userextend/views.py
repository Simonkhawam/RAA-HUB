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



    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(
                commit=False)

            subject = 'Noul tau cont!'  # se poate scrie orice ca subiect
            message = f"""Felicitari {new_user.first_name} {new_user.last_name},
            Contul tau a fost creat cu succes!

            Pentru autentificare te rog sa te loghezi la linkul de mai jos: 
            
            https://raahub-16a5dd72bf90.herokuapp.com
            """
            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])

        return redirect('login')

