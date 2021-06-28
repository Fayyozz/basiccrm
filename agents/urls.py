from django.urls import path

from agents.views import AgentListView, AgentCreateView, AgentDeleteView, AgentDetailView

app_name = 'agents'
urlpatterns = [
    path('', AgentListView.as_view(), name='list'),
    path('create/', AgentCreateView.as_view(), name='create'),
    path("<int:id>/delete/", AgentDeleteView.as_view(), name='delete'),
    path('<int:id>/detail/', AgentDetailView.as_view(), name='detail')
]