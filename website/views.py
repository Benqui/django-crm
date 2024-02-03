from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecord
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records':records})

# def login_usr(request):
#     pass

def logout_usr(request):
    logout(request)
    messages.success(request, "Bye bye we vuelva pronto :)")
    return redirect('home')


def register_usr(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "te registraste correctamente we holi :) ")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})


def  customer_record(request, pk):
    if request.user.is_authenticated:
        #checar los records
        cust_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':cust_record})
    else:
        messages.success(request, "Nmms no tas loggiado que haces aqui we >:(")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Elemento eliminado con exito")
        return redirect('home')
    else:
        messages.success(request, "Nmms no tas loggiado que haces aqui we >:(")
        return redirect('home')
    
def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Elemento agregado")
                return redirect('home')
        return render(request, 'add_record.html',{'form':form})
    else:
        messages.success(request, "saquese chamaco mugroso")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current)
        if form.is_valid():
            form.save()
            messages.success(request,"Elemento actualizado correctamente")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.success(request, "Nmms no tas loggiado que haces aqui we >:(")
        return redirect('home')
    