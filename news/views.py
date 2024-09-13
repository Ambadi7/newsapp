

from django.shortcuts import render
from .services import fetch_latest_news

def news_view(request):
    query = request.GET.get('query', 'latest')  # Get search query
    articles = fetch_latest_news(query)  # Fetch news from GNews API
    return render(request, 'news/news_list.html', {'articles': articles, 'query': query})
