from django.shortcuts import render, redirect
from .forms import EncostaForm, EncostaFormUpdate, denunciaForm, Regular_user_registration_form, Engineer_registration_form
from django.contrib import messages
from .models import Encosta, User, Regular_user, Engineer
from django.views.generic import CreateView



def IndexView(request):
  return render(request, 'index.html')

def EncostaView(request):
  encostas = Encosta.objects.all()
  return render(request, 'crud.html', {'encostas': encostas})


# create view
def CreateEncostaView(request):
  form = EncostaForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_add.html', {'form': form})

def UpdateEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  form = EncostaFormUpdate(request.POST or None, instance=encosta)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_upd.html', {'form': form, 'encosta': encosta})


# delete view
def DeleteEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  if request.method == 'POST':
    encosta.delete()
    return redirect('crud')
  return render(request, 'encosta_del.html', {'encosta': encosta})


# Visualizar encosta selecionada
def EncostaSelecionadaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  return render(request, 'encosta_selecionada.html', {'encosta': encosta})



def DenunciaFormView(request):
  if request.method == 'GET':
    form = denunciaForm()
    return render(request,"denuncia_formulario.html",context ={'form': form})
  else:
    form = denunciaForm(request.POST)

    if form.is_valid():
      formulario = form.save()
      form = denunciaForm()
      messages.success(request, 'Seu reporte foi feito com sucesso')
      
      return render(request, 'denuncia_formulario.html', {'form': form})
    else:
      messages.error(request, 'Invalid form submission.')
      messages.error(request, form.errors)
    return render(request,"denuncia_formulario.html",context ={'form': form})
  

def register(request):
  return render(request, '../templates/register.html')

class User_register(CreateView):
  model = User
  form_class = Regular_user_registration_form
  template_name = "../templates/user_register.html"

class Engineer_register(CreateView):
  model = User
  form_class = Engineer_registration_form
  template_name = "../templates/engineer_register.html"