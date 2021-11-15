from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainTemplateView.as_view(), name='main'),
    path('agents/<subjob_id>', views.agents, name='agents')
]