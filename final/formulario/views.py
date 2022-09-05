import http
from turtle import st 
from django.http import HttpResponse
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from datetime import datetime, timedelta
from django.contrib import messages
from pandas.tseries.offsets import BDay, BMonthEnd
from .models import Form





def home(request):
    if request.method == "POST":
        carnet = request.POST["carnet"]
        name = request.POST["name"]
        addres = request.POST["addres"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        age = request.POST["age"]
        career = request.POST["career"]
        options = request.POST["options"]
        if validation(carnet): 
            if edad(age):
                programacion =aprovacion(carnet, options)
                register = Form.objects.creacion(carnet, name, addres, phone, gender, age, career, options, programacion )
                #datos = Form.objects.all()
                messages.success(request, "felicidades se a registrado con exito :D  ") 
                return HttpResponse(f"querido usuario {name} su fecha de declamacion es: {programacion}")
                #return render(request, "formulario/muestra.html", {"datos": datos} ) 
                
                

            else:
                messages.error(request, "el usuario debe ser mayor a 17 años ") 
                
        else: 
             messages.error(request, "carnet inconrecto, ejemplo de uno valido A15231, al final solo usar 1, 3, o 9, no usa 0 ")  
                
        return render(request, "formulario/formulario.html"  )   
           
           
    else:
        messages.error(request, "el carnet es incorrecto ")
        
        
        return render(request, "formulario/formulario.html"  )
def validation(carnet):
    if carnet[0] =="A" and carnet[2] == "5" and "0" not in carnet:
        if carnet[5] == "1" or carnet[5] == "3" or carnet[5] == "9":
            return True
        else: 
            return False
    else:
        return False
              
                     
def edad(age):
    actual = datetime.now()
    fecha = datetime.strptime(age, '%Y-%m-%d')
    resul = relativedelta(actual,fecha)
    if resul.years > 17:
        return True
    else:
        return False
    
def aprovacion(carnet, option):
    actual = datetime.now()
    if carnet[5] == "1" and  option == "2":
        dia = actual + BDay(5)
        return str(dia)[0:10] 
    elif carnet[5] == "3" and option == "1":
        mes = BMonthEnd().rollforward(actual)
        return str(mes)[0:10] 
    else:
        viernes = actual + timedelta( (4-actual.weekday()) % 7 )
        return str(viernes)[0:10]
 
def entrega(request):
    datos = Form.objects.all()
        
    return  render(request, "formulario/entrega.html" , {"datos":datos})   
    
    
    