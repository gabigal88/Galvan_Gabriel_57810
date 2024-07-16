from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Copyright Gabriel Galvan

def home(request):
    return render(request, "AppCoder/home.html")

def acerca(request):
    return render(request, "AppCoder/acerca.html")

#____Circuitos
def circuitos(request):
    contexto={"circuitos":Circuito.objects.all()}
    return render(request, "AppCoder/circuitos.html",contexto)



#____Rental
@login_required
def rental(request):
    contexto={"rental":Rental.objects.all()}
    return render(request, "AppCoder/rental.html",contexto)

@login_required
def formulario_rental(request):
    if request.method=='POST':
        rentalForm=RentalFormulario(request.POST)
        print(rentalForm)
        if rentalForm.is_valid: 
            informacion=rentalForm.cleaned_data
            rental=Rental(equipos=informacion['equipos'],cant_dias=informacion['cant_dias'],valor=informacion['valor'])
            rental.save()
            contexto={"rental":Rental.objects.all()}
            return render(request,"AppCoder/rental.html")
    else:
        rentalForm=RentalFormulario()
    return render(request,"AppCoder/rent_Form.html", {"rentalForm": rentalForm})


#____Clientes

class ClienteList(LoginRequiredMixin,ListView):
    model=Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nombre","apellido","identificacion","email","telefono"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "identificacion", "email", "telefono"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")

@login_required
def buscarClientes(request):
    return render(request,"AppCoder/buscar_cliente.html") #ok

@login_required
def encontrarClientes(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'cliente': clientes}
    else:
        contexto = {'cliente': Cliente.objects.all()}
    return render(request,"AppCoder/clientes.html",contexto)


#____bicicletas

class BicicletaList(LoginRequiredMixin,ListView):
    model=Bicicleta

class BicicletaCreate(LoginRequiredMixin, CreateView):
    model = Bicicleta
    fields = ["marca", "modelo", "serie", "suspension","imagen"]
    success_url = reverse_lazy("bicicletas")

class BicicletaUpdate(LoginRequiredMixin, UpdateView):
    model = Bicicleta
    fields = ["marca", "modelo", "serie", "suspension","imagen"]
    success_url = reverse_lazy("bicicletas")

class BicicletaDelete(LoginRequiredMixin, DeleteView):
    model = Bicicleta
    success_url = reverse_lazy("bicicletas")

def buscarBicicletas(request):
    return render(request,"AppCoder/buscar_bicicleta.html") #ok

def encontrarBicicletas(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        bicicletas = Bicicleta.objects.filter(marca__icontains=patron)
        contexto = {'bicicleta': bicicletas}
    else:
        contexto = {'bicicleta': Bicicleta.objects.all()}
    return render(request,"AppCoder/bicicletas.html",contexto)


#____Accesorios

class AccesoriosList(LoginRequiredMixin,ListView):
    model=Accesorios

class AccesoriosCreate(LoginRequiredMixin, CreateView):
    model = Accesorios
    fields = ["tipo", "marca"]
    success_url = reverse_lazy("accesorios")

class AccesoriosUpdate(LoginRequiredMixin, UpdateView):
    model = Accesorios
    fields = ["tipo", "marca"]
    success_url = reverse_lazy("accesorios")

class AccesoriosDelete(LoginRequiredMixin, DeleteView):
    model = Accesorios
    success_url = reverse_lazy("accesorios")

def buscarAccesorios(request):
    return render(request,"AppCoder/buscar_accy.html") #ok

def encontrarAccesorios(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        accesorios = Accesorios.objects.filter(tipo__icontains=patron)
        contexto = {'accesorio': accesorios}
    else:
        contexto = {'accesorio': Accesorios.objects.all()}

    return render(request,"AppCoder/accesorios.html",contexto)



# ___Login Logout y registracion

def loginRequest(request):
    if request.method== "POST":
         usuario=request.POST["username"]
         clave=request.POST['password']
         user=authenticate(request,username=usuario,password=clave)
         if user is not None:
             login(request,user)

             try:
                 avatar=Avatar.objects.get(user=request.user.id).imagen.url
             except:
                 avatar="/media/avatares/default.jpg"
             finally:
                 request.session["avatar"]=avatar
             return render(request,"AppCoder/index.html")
         else:
             return redirect(reverse_lazy('login'))
    
    else:
         miForm= AuthenticationForm()
         
    return render(request,"AppCoder/login.html", {"form":miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "AppCoder/registro.html", {"form": miForm})
 

#__edicion de perfil 
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "AppCoder/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppCoder/cambiar_clave.html"
    success_url = reverse_lazy("home")

#__agregar avatar


def agregarAvatar(request):
    usuario = request.user
    if request.method == "POST":
        miForm = AvatarForm(request.POST,request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen=miForm.cleaned_data["imagen"]
            #____borrar viejos
            avatarViejo=Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar=Avatar(user=usuario,imagen=imagen)
            avatar.save()
        #__enviar imagen al home
            imagen=Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"]=imagen

            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "AppCoder/agregarAvatar.html", {"form": miForm})