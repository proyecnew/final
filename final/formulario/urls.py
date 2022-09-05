from django.urls import path
from .views import home, entrega 

urlpatterns = [
    path('', home , name="home"),
    path('entrega/', entrega , name="entrega"),

]