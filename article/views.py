from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Article

class IndexView(generic.ListView):
    template_name = "index.html"
    paginate_by = 10
    
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Article
    template_name = "details.html"
