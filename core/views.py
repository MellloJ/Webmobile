from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

class Login(View):
    def get(self, request):

        if request.user.is_authenticated:
            return render(request, 'login.html', {'success': 'Usuário já está logado!'})
        else:
            return render(request, 'login.html')
        
    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login.html', {'success': 'Usuário logado com sucesso!'})
            else:
                return render(request, 'login.html', {'error': 'O usuário não está ativo!'})
        else:
            return render(request, 'login.html', {'error': 'Nome de usuário ou senha incorretos!'})

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse(''))
        else:
            return redirect(reverse(''))