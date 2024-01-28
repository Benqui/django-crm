from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    # checar si tas logeado o no we 
    if request.method=='POST':
        username = request.POST['usrname']
        passwd = request.POST['password']
        #auth
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request, "Tas loggeado bienvenido :) ")
            return redirect('home')
        else:
            messages.success(request, "Error al loggearte quien ere we!! >:(")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_usr(request):
#     pass

def logout_usr(request):
    logout(request)
    messages.success(request, "Bye bye we vuelva pronto :)")
    return redirect('home')


def register_usr(request):
    return render(request, 'register.html',{})