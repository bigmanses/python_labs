from django.shortcuts import render
from .models import Newss


# Create your views here.
def news_home(req):
    news = Newss.objects.order_by('date')
    return render(req, 'news/news_home.html', {'news': news})

def create_news(req):
    news = Newss.objects.order_by('date')
    return render(req, 'news/create.html')
