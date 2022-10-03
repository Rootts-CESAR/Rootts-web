from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include

from .views import Engineer_register, IndexView, EncostaView, CreateEncostaView, UpdateEncostaView, DeleteEncostaView, DenunciaFormView, EncostaSelecionadaView, User_register, register,logged


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView, name='index'),
    path('crud/', EncostaView, name='crud'),
    path('create/', CreateEncostaView, name='add_encosta'),
    path('update/<int:pk>/', UpdateEncostaView, name='upd_encosta'),
    path('delete/<int:pk>/', DeleteEncostaView, name='del_encosta'),
    path('encosta/<int:pk>/', EncostaSelecionadaView, name='view_encosta'),
    path('denuncia_formulario/',DenunciaFormView, name='DenunciaForm'),
    path('logged/',logged, name='logged'),
    path('register/', register ,name='register'),
    path('user_register/', User_register.as_view() ,name='user_register'),
    path('engineer_register/', Engineer_register.as_view() ,name='engineer_register')
]
