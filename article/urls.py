from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('<str:slug>', views.Details.as_view(), name = 'details')
]