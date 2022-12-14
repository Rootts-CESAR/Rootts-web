from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import user_passes_test


from .forms import *
from .models import *

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



def EncostaGeneratePDf(request, pk):
  buf = io.BytesIO()
  c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
  textob = c.beginText()
  textob.setTextOrigin(inch, 2.5 * inch)
  textob.setFont("Helvetica", 14)
  encostas = Encosta.objects.get(id=pk)

  c.setFillColorRGB(0, 0, 0)
  c.setFont("Helvetica-Bold", 16)
  c.drawCentredString(300, 100, "Relatório de Risco de Deslizamento de Encosta")

  c.setFont("Helvetica", 14)
  c.drawCentredString(300, 125, "Dados do Relatório Encosta: " + encostas.nome)


  c.setFillColorRGB(0, 0.75, 0)
  c.setFont("Helvetica-Bold", 20)
  c.drawCentredString(100, 50, "Rootts")

  if encostas.prioridadeEncosta == 'Baixo':
    c.setFillColorRGB(0, 0.75, 0)
    c.drawCentredString(500, 50, "Baixa")
  elif encostas.prioridadeEncosta == 'Médio':
    c.setFillColorRGB(1, 0.75, 0)
    c.drawCentredString(500, 50, "Média")
  elif encostas.prioridadeEncosta == 'Alto':
    c.setFillColorRGB(1, 0, 0)
    c.drawCentredString(500, 50, "Alta")
  elif encostas.prioridadeEncosta == 'Crítico':
    c.setFillColorRGB(1, 0, 0)
    c.drawCentredString(500, 50, "Crítica")
  elif encostas.prioridadeEncosta == 'Muito Baixa':
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(500, 50, "Muito Baixa")

  c.setFillColorRGB(0, 0, 0)


  lines = []

  lines.append("Endereço: " + str(encostas.local))
  lines.append("Latitude: " + str(encostas.latitude))
  lines.append("Longitude: " + str(encostas.longitude))
  lines.append("Declividade: " + str(encostas.declividade))
  lines.append("Coeficiente de Umidade: " + str(encostas.coeficienteUmidade))
  lines.append("Número de Construções por m²: " + str(encostas.numeroConstrucoes))
  lines.append("Proximidade de Redes Viarias por m²: " + str(encostas.proximidadeRedeViarias))
  lines.append("Proximidade de Corpos Liquidos por m²: " + str(encostas.proximidadeCorposLiquidos))

  for i in lines:
    textob.textLine(i)
  
  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)

  return FileResponse(buf, as_attachment=True, filename='Encosta_' + str(encostas.id) + '.pdf')



def IndexView(request):
  return render(request, 'index.html')

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_engineer, login_url='/login/')
def EncostaView(request):
  encostas = Encosta.objects.all()
  return render(request, 'crud.html', {'encostas': encostas})


class EncostaSearchView(ListView):
  model = Encosta
  template_name = 'crud.html'
  context_object_name = 'encostas'

  def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = Encosta.objects.filter(
      Q(nome__icontains=query) | Q(local__icontains=query)
    )

    return object_list


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_engineer, login_url='/login/')
def CreateEncostaView(request):
  form = EncostaForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_add.html', {'form': form})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_engineer, login_url='/login/')
def UpdateEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  form = EncostaFormUpdate(request.POST or None, instance=encosta)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_upd.html', {'form': form, 'encosta': encosta})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_engineer, login_url='/login/')
def DeleteEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  if request.method == 'POST':
    encosta.delete()
    return redirect('crud')
  return render(request, 'encosta_del.html', {'encosta': encosta})


# Visualizar encosta selecionada
@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_engineer, login_url='/login/')
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
      form.save()
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


def EngenheiroFormView(request):
  forms = Formulario_denuncia.objects.all()
  if request.method == "POST":
    # Get list of checked box id's
    id_list = request.POST.getlist('boxes')

    # Uncheck all events
    forms.update(aprovado=False)

    # Update the database
    for x in id_list:
      Formulario_denuncia.objects.filter(pk=int(x)).update(aprovado=True)
  
    # Show Success Message and Redirect
    return render(request, 'aprovados.html', {'forms':forms})
  else:
    return render(request, 'engineerFormulario.html', {'forms':forms})
  return render(request, 'engineerFormulario.html', {'forms':forms})

def DescricaoView(request,pk):
  forms = Formulario_denuncia.objects.get(id=pk)
  return render(request, 'formulario_selecionado.html', {'forms':forms})


def DeleteformView(request, pk):
  forms = Formulario_denuncia.objects.get(id=pk)
  if request.method == 'POST':
    forms.delete()
    return redirect('EngenheiroForm')
  return render(request, 'form_del.html', {'forms': forms})


def RiscoView(request):
  encostas = Encosta.objects.all()
  return render(request, 'risco_deslizamento.html', {'encostas': encostas})

class RiscoSearchView(ListView):
  model = Encosta
  template_name = 'risco_deslizamento.html'
  context_object_name = 'encostas'

  def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = Encosta.objects.filter(
      Q(nome__icontains=query) | Q(local__icontains=query) | Q(prioridadeEncosta__icontains=query)
    )

    return object_list
