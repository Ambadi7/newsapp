import requests
from django.conf import settings

def fetch_latest_news(query=""):
    url = f'https://gnews.io/api/v4/search?q={query}&token={settings.GNEWS_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    return []
