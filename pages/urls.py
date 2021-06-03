from django.urls import path
from pages.views import HomeView, LoginView, AddClientView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('add-client', AddClientView.as_view(), name="add_client")
]