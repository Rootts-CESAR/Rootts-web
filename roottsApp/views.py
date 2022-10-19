from django.views.generic import CreateView
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login

from .forms import *
from .models import *


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
      messages.success(request, 'Seu relatório foi feito com sucesso')
      
      return render(request, 'denuncia_formulario.html', {'form': form})
    else:
      messages.error(request, 'Preencha o formulario corretamente')
      # messages.error(request, form.errors)
    return render(request,"denuncia_formulario.html",context ={'form': form})
  

# tratamento de erro

def error_404_view(request, exception):
  return render(request,'404.html', status = 404)

def error_401_view(request, exception):
  return render(request,'401.html', status = 401)

class User_register(CreateView):
  model = RegularUser
  form_class = RegularUserCreationForm
  template_name = "../templates/user_register.html"

  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'regular_user'
    return super().get_context_data(**kwargs)

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('index')


class Engineer_register(CreateView):
  model = EngineerUser
  form_class = EngineerUserCreationForm
  template_name = "../templates/engineer_register.html"

  def get_context_data(self, **kwargs):
    kwargs['user_type'] = 'engineer_user'
    return super().get_context_data(**kwargs)

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect('index')


def register(request):
  return render(request, '../templates/register.html')



def login_view(request):
  username = request.POST['username']
  email = request.POST.get('email')
  password = request.POST.get('password')
  user = authenticate(request, username=username, email=email, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return redirect('index')
    else:
      return render(request, '../templates/login.html', {'error_message': 'Sua conta foi desativada'})
  else:
    return render(request, '../templates/login.html', {'error_message': 'Login invalido'})


@login_required
def logout_view(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('index')


