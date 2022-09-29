from django.shortcuts import render

# Create your views here
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Encosta


class IndexView(ListView):
    model = Encosta
    template_name = 'index.html'
    context_object_name = 'Encostas'


class EncostaView(ListView):
    models = Encosta
    template_name = 'crud.html'
    queryset = Encosta.objects.all()
    context_object_name = 'encostas'


class CreateEncostaView(CreateView):
    model = Encosta
    template_name = 'encosta_form.html'
    fields = ['nome', 'descricao', 'local']
    success_url = reverse_lazy('crud')


class UpdateEncostaView(UpdateView):
    model = Encosta
    template_name = 'encosta_form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('crud')


class DeleteEncostaView(DeleteView):
    model = Encosta
    template_name = 'encosta_del.html'
    success_url = reverse_lazy('crud')

