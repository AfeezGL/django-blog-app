from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('article/<str:slug>', views.Details.as_view(), name = 'details'),
    path('search', views.Search, name = 'search')
]