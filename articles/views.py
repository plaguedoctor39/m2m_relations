from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    scopes = list(ArticleScope.objects.all())
    articles = list(Article.objects.order_by(ordering))
    context = {'object_list': articles,
               'scopes': scopes
               }
    print(scopes)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
