from django.shortcuts import render


# Create your views here.
def news_home(req):
    return render(req, 'newsApp/about.html')
