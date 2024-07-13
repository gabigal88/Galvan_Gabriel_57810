from django.urls import path
from AppCoder.views import *
#from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home,name="home"),

    #__clientes
    
    path('clientes', ClienteList.as_view(), name="clientes"),
    path('clienteCreate/', ClienteCreate.as_view(), name="clienteCreate"),
    path('clienteUpdate/<int:pk>/', ClienteUpdate.as_view(), name="clienteUpdate"), 
    path('clienteDelete/<int:pk>/', ClienteDelete.as_view(), name="clienteDelete"),
    path('buscarClientes/', buscarClientes,name="buscarClientes"),
    path('encontrarClientes/', encontrarClientes,name="encontrarClientes"),

    #____circuitos
    path('circuitos', circuitos, name="circuitos"),

    #____bicicletas
    path('bicicletas', BicicletaList.as_view(), name="bicicletas"),
    path('bicicletaCreate/', BicicletaCreate.as_view(), name="bicicletaCreate"), 
    path('bicicletaUpdate/<int:pk>/', BicicletaUpdate.as_view(), name="bicicletaUpdate"), 
    path('bicicletaDelete/<int:pk>/', BicicletaDelete.as_view(), name="bicicletaDelete"),
    path('buscarBicicletas/', buscarBicicletas,name="buscarBicicletas"),
    path('encontrarBicicletas/', encontrarBicicletas,name="encontrarBicicletas"),

    #____accesorios
    path('accesorios', AccesoriosList.as_view(), name="accesorios"),
    path('accesoriosCreate/', AccesoriosCreate.as_view(), name="accesoriosCreate"), 
    path('accesoriosUpdate/<int:pk>/', AccesoriosUpdate.as_view(), name="accesoriosUpdate"), 
    path('accesoriosDelete/<int:pk>/', AccesoriosDelete.as_view(), name="accesoriosDelete"),
    path('buscarAccesorios/', buscarAccesorios,name="buscarAccesorios"),
    path('encontrarAccesorios/', encontrarAccesorios,name="encontrarAccesorios"),


    path('rental', rental,name="rental"),
    path('rent_Form', formulario_rental,name="rent_Form"),

    path('acerca', acerca,name="acerca"),

    #___ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #__Edicion de perfil / Avatar
    path('editarPerfil/', editProfile, name="editarPerfil"),
    path('cambiar_clave/<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    #path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]