from django.urls import path
from pages.views import HomeView, LoginView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login')
]