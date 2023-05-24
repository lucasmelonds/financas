from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Receita, Despesa, Balanco, Titulo, Usuario

def index(request):
    lista_receita = Receita.objects.all()[:25]
    lista_despesa = Despesa.objects.all()[:25]
    lista_balanco = Balanco.objects.all()[:25]
    lista_titulo = Titulo.objects.all()[:25]
    context = {
        "lista_receita": lista_receita,
        "lista_despesa": lista_despesa,
        "lista_balanco": lista_balanco,
        "lista_titulo": lista_titulo,
        }
    return render(request, 'financas/index.html', context)

def detalhes (request, balanco_id):
    titulo = get_object_or_404(Titulo, pk = balanco_id)
    return render(request, 'financas/detalhes.html', {'titulo': titulo})

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/index.html')
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(Usuario, usuario=request.POST['username'])
        if user.senha != request.POST['password']:
            return render(request, 'financas/index.html')
        request.session['id_user'] = user.id
        return render(request, 'financas/detalhes.html')

class Cadastrar(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/index.html')
    def post(self, request, *args, **kwargs):
        usuario = Usuario(usuario = request.POST['user'], senha = request.POST['password'])
        usuario.save()
        request.session['id_user'] = usuario.id
        return render(request, 'financas/detalhes.html')

def Logout(request):
    del request.session['id_user']
    return render(request, 'financas/index.html')