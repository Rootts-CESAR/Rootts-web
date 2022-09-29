from django.urls import path

from .views import IndexView, EncostaView, CreateEncostaView, UpdateEncostaView, DeleteEncostaView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('crud/', EncostaView.as_view(), name='crud'),
    path('add/', CreateEncostaView.as_view(), name='add_encosta'),
    path('<int:pk>/update/', UpdateEncostaView.as_view(), name='upd_encosta'),
    path('<int:pk>/delete/', DeleteEncostaView.as_view(), name='del_encosta'),
]
