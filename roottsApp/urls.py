from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView, name='index'),
    path('crud/', EncostaView, name='crud'),
    path('create/', CreateEncostaView, name='add_encosta'),
    path('update/<int:pk>/', UpdateEncostaView, name='upd_encosta'),
    path('delete/<int:pk>/', DeleteEncostaView, name='del_encosta'),
    path('encosta/<int:pk>/', EncostaSelecionadaView, name='view_encosta'),
    path('denuncia_formulario/',DenunciaFormView, name='DenunciaForm'),
    path('new_variable/<int:pk>/',newVariableView, name='AddNewVariableToEncosta'),
    path('register/', register ,name='register'),
    path('user_register/', User_register.as_view() ,name='user_register'),
    path('engineer_register/', Engineer_register.as_view() ,name='engineer_register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]
handler404 = "roottsApp.views.error_404_view"
handler404 = "roottsApp.views.error_401_view"
