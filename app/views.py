from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def contacts(request):

    params={
        'tel':911111111
    }
    print("########")
    return render(request,'Contactos.html',params)

def perfil(request):
    return render(request,'MeuPerfil.html',{})
