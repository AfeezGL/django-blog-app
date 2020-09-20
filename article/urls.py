from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<str:slug>/', views.DetailView.as_view(), name = 'details'),

]