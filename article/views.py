from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class Index(ListView):
    template_name = "index.html"
    paginate_by = 5
    def get_queryset(self):
        return Article.objects.order_by("-pub_date")
        
class Details(DetailView):
    model = Article
    template_name = "details.html"