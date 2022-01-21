from .models import Usuarios, Login_view
from django import forms 
from django.core.exceptions import ValidationError

def validate_password(pasword):
    if len(pasword)<8:
        raise ValidationError('El minimo de caracteres son 8')

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"
        widgets ={'usuario': forms.TextInput(attrs = {'placeholder':'Usuario'}), 
        'nombre': forms.TextInput(attrs = {'placeholder':'Nombre'}),
        'apellidos': forms.TextInput(attrs = {'placeholder':'Apellidos'}),
        'correo': forms.TextInput(attrs = {'placeholder':'Correo'}),
        'password': forms.TextInput(attrs = {'placeholder':'Password'})
        }
    def __init__(self, *args, **kwargs):
        super(UsuarioModelForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs.update({'class':'formu'}) 
        self.fields['usuario'].label = ''       
        self.fields['nombre'].widget.attrs.update({'class':'formu'})
        self.fields['nombre'].label = ''
        self.fields['apellidos'].widget.attrs.update({'class':'formu'})
        self.fields['apellidos'].label = ''
        self.fields['correo'].widget.attrs.update({'class':'formu'})
        self.fields['correo'].label = ''
        self.fields['password'].widget.attrs.update({'class':'formu'})
        self.fields['password'].label = ''
        self.fields['tipo'].widget.attrs.update({'class':'formu'})
        self.fields['tipo'].label = ''
    def clean(self):
        super().clean()

class Login(forms.ModelForm):
    class Meta:
        model = Login_view
        fields = "__all__"
        widgets ={'usuario': forms.TextInput(attrs = {'placeholder':'Usuario'}),
        'password': forms.TextInput(attrs = {'placeholder':'Password'})
        }
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs.update({'class':'formu'})
        self.fields['usuario'].label = '' 
        self.fields['password'].widget.attrs.update({'class':'formu'})
        self.fields['password'].label = '' 

    def clean(self):
        super().clean()