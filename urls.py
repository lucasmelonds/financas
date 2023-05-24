from django.urls import path
from . import views

app_name = 'financas'
urlpatterns = [
    # ex.:/
    path('', views.index, name='index'),
    path(
        'financas/<int:balanco_id>/',
        views.detalhes,
        name='detalhes'),

    path('financas/login/', views.Login.as_view(), name='Login'),
    path('financas/signup/', views.Cadastrar.as_view(), name='Cadastrar'),
    path('financas/logout/', views.Logout, name='Logout'),
]
