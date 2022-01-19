from .models import Usuarios, Login_view
from django import forms 


class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"

class Login(forms.ModelForm):
    class Meta:
        model = Login_view
        fields = "__all__"