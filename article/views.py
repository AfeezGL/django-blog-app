from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Article

class Index(ListView):
    template_name = "index.html"
    paginate_by = 10
    def get_queryset(self):
        return Article.objects.order_by("-pub_date")
        
class Details(DetailView):
    model = Article
    template_name = "details.html"
    
def Search(request):
    template = "index.html"
    query = request.GET["query"]
    queries = query.split(" ")
    print (queries)
    article_list = []
    for query in queries:
        articles = Article.objects.filter(Q(title__icontains = query))
        for article in articles:
            article_list.append(article)
    object_list = article_list
    return render(request, template, {"object_list": object_list})