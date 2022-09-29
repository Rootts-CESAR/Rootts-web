from django.urls import path

from .views import IndexView, ProdutoView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('crud/', ProdutoView.as_view(), name='crud'),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
]
