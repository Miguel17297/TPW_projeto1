from django.shortcuts import render
from app.forms import *
from app.models import *

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

def servicosEnf(request):

    return render(request,'servicosEnf.html',{})

def servicosAdmin(request):
    return render(request, 'servicosAdmin.html', {})

def especialiades(request):
    return render(request, 'especialidades.html', {})

def register(request):
    account=None

    if request.method=="POST":
            form=accountForm(request.POST)

            if form.is_valid():
                #buscar os dados do form
                email=form.cleaned_data['email']
                passw=form.cleaned_data['password']
                nmec=form.cleaned_data['nmec']
                nome=form.cleaned_data['nome']
                cc =form.cleaned_data['cc']
                especialidade=form.cleaned_data['especialidade']
                gabinte=form.cleaned_data['gabinte']
                cedula=form.cleaned_data['cedula']

            if especialidade==None and gabinte==None: # se não tiver especialidade nem gabinete é enfermeiro
                account=Enfermeiro()

            else:
                account=Medico()
                account.gabinte=gabinte
                account.especialidade=especialidade

            account.email=email
            account.password=passw
            account.nmec=nome
            account.nome=nome
            account.cc=cc
            account.ncedulaprofissional=cedula
            account.save()
            return  render(request,'login.html',{})
    else:
        form=accountForm()
        return render(request,'register.html',{'form':form})

