from django.shortcuts import render

from django.http import HttpResponse

from django.views import generic

from .models import Article

from hitcount.views import HitCountDetailView

class IndexView(generic.ListView):
    template_name = "index.html"
    paginate_by = 10
    
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

class DetailView(HitCountDetailView):
    model = Article
    template_name = "details.html"
    count_hit = True 