from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    identificacion=models.IntegerField()
    email=models.EmailField()
    telefono=models.IntegerField()
    fecha=models.DateField()
    bicicleta=models.CharField(max_length=40)
    accesorios=models.CharField(max_length=40)

    #class Meta:
        #ordering=["identificacion"]
    
    def __str__(self):
        return f'{self.nombre},{self.apellido},{self.identificacion},{self.email},{self.telefono},{self.fecha},{self.bicicleta},{self.accesorios}'

class Bicicleta(models.Model):
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    serie=models.CharField(max_length=20)
    suspension=models.CharField(max_length=20)
    imagen=models.ImageField(verbose_name="Imagen", upload_to='bicicletas')
    def __str__(self):
        return f'{self.marca},{self.modelo},{self.serie},{self.suspension},{self.imagen}'

class Accesorios(models.Model):
    tipo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.tipo},{self.marca}'

    class Meta:
        verbose_name="Accesorios"
        verbose_name_plural="Accesorios"
        ordering=["tipo","marca"]

class Rental(models.Model):
    equipos=models.CharField(max_length=30)
    cant_dias=models.IntegerField()
    valor=models.IntegerField()
    def __str__(self):
        return f'{self.equipos},{self.cant_dias},{self.valor}'
    

class Circuito(models.Model):
    sendero=models.CharField(max_length=30)
    dificultad=models.CharField(max_length=30)
    distancia=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.sendero},{self.dificultad},{self.distancia}'


class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} - {self.imagen}'