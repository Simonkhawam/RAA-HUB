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

            subject = '🎉 Contul tău a fost creat cu succes!'  # se poate scrie orice ca subiect
            message = f"""
            <html>
            <head></head>
            <body>
                <p><strong>Felicitări {new_user.first_name},</strong></p>
                <p>Pentru autentificare, te rog să te loghezi folosind link-ul de mai jos:</p>
                <p><a href="https://raahub-16a5dd72bf90.herokuapp.com/login/" target="_blank">
                    https://raahub-16a5dd72bf90.herokuapp.com/login/</a></p>
                <p><strong>Bun venit în echipa RAA!</strong></p>
            </body>
            </html>
            """

            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email], html_message=message)

        return redirect('login')