from django.shortcuts import render, reverse
from django.views import View
from pages.forms import ClientForm


class HomeView(View):
    def get(self, request):
        return render(request, 'pages/home.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')


class AddClientView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'pages/add-client2.html', {'form': form})
