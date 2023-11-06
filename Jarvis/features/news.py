import requests
import json



def get_news():
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d9bf7ec36a8e4655843baaa65011f305'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d9bf7ec36a8e4655843baaa65011f305'
