from django.shortcuts import render, reverse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'pages/home.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')