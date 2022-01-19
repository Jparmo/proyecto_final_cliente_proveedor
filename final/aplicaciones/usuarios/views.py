from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UsuarioModelForm, Login

# Create your views here.
def login_view(request):
    # inicio de sesion
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username = username, password = password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('bienvenida')
    #     else:
    #         return render(request, 'login.html', {'error':'Ingresaste informacion invalida'})
    # return render(request, 'login.html')
    form = Login()
    return render(request, 'login.html', {"form":form})

def register_view(request):
    #registro
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = User.objects.create_user(username=username,email=email,password=password)
    #     user.first_name = request.POST['first_name']
    #     user.last_nasme = request.POST['last_name']
    #     if 'cliente' in request.POST:
    #         user.is_client = True
    #     if 'proveedor' in request.POST:
    #         user.is_proveedor = True
    #     user.save()
    #     return redirect('bienvenida')
    # return render(request,'register.html')
    form = UsuarioModelForm()
    return render(request, 'register.html', {"form":form})

def logout_view(request):
    #cierre de sesion
    logout(request)
    return redirect('login.html')