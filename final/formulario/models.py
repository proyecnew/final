from django.db import models

genero = [
    [0, "Hombre"],
    [1, "mujer"]
]

opcion_usuario =[
    [0, "lirica"],
    [1, "epica"],
    [2, "dramatica"]
]

class Muestra(models.Manager):
    def creacion(self,carnet,name,addres,phone,gender, age,career,options,fecha_declaracion):
        print(carnet,name,addres, phone,gender,  age, career, options, fecha_declaracion)
        valor = self.create(carnet= carnet,name = name, addres = addres, gender = gender, phone = phone, age = age, career = career, options = options, fecha_declaracion = fecha_declaracion   )
        return valor
        
        

class Form(models.Model):
    carnet = models.CharField(max_length=6, null=False)
    name = models.CharField(max_length=40, null=False)
    addres = models.CharField(max_length=40, null=False)
    gender = models.IntegerField(choices=genero, null=False)
    phone = models.CharField(max_length=8, null=False)
    age = models.DateField( null=False)
    career = models.CharField(max_length=50, null=False)
    options = models.IntegerField(choices=opcion_usuario, null=False)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    fecha_declaracion = models.DateField()
    
    objects = Muestra()
    def __str__(self):
        return self.carnet