from django.urls import path

from .views import IndexView, EncostaView, CreateEncostaView, UpdateEncostaView, DeleteEncostaView, DenunciaFormView, EncostaSelecionadaView


urlpatterns = [
    path('', IndexView, name='index'),
    path('crud/', EncostaView, name='crud'),
    path('create/', CreateEncostaView, name='add_encosta'),
    path('update/<int:pk>/', UpdateEncostaView, name='upd_encosta'),
    path('delete/<int:pk>/', DeleteEncostaView, name='del_encosta'),
    path('encosta/<int:pk>/', EncostaSelecionadaView, name='view_encosta'),
    path('denuncia_formulario/',DenunciaFormView, name='DenunciaForm'),
]
