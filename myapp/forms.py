from django import forms
from .models import Comanda, Utilizator

class ComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}),
            'agent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agent Name'}),
            'code_art': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Article Code'}),
            'order_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Order Number'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'final_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Final Quantity'}),
            'order_type': forms.Select(attrs={'class': 'form-select'}),
            'dimension': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter size, e.g., 50mm',
                'pattern': r'^\d+mm$',
                'title': 'Dimensions should be in the format "50mm".'
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class UtilizatorForm(forms.ModelForm):
    class Meta:
        model = Utilizator
        fields = '__all__'
        widgets = {
            'prenume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'parola': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'tip_statie': forms.Select(attrs={'class': 'form-select'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
        }
