from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create_news, name='create'),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail')
]