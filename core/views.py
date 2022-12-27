from django.views.generic import View
from django.shortcuts import render
#Hay 2 tipos de vistas, clases y funciones esta es de clases
class HomeView(View): #HomeView da acceso a ambos, get req y post req. Get request pide la info para tu ver, post request es lo que envias para que el servidor haga algo con esa información
    def get(self, request, *args, **kwargs):
        context={

        }

        return render(request, 'index.html', context) #Las '' son el template osea la info en html que se mostrará. También podria definirse context como doble break pero en este caso lo dejamos así, como variable