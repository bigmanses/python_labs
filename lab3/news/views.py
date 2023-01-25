from django.shortcuts import render, redirect
from .models import Newss
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(req):
    news = Newss.objects.order_by('date')
    return render(req, 'news/news_home.html', {'news': news})


class NewDetailView(DetailView):
    model = Newss
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewUpdateView(UpdateView):
    model = Newss
    template_name = 'news/create.html'
    form_class = NewsForm


class NewDeleteView(DeleteView):
    model = Newss
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create_news(req):
    erorr = ''
    if req.method == 'POST':
        form = NewsForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            erorr = 'Неправильно заполненная форма'
    form = NewsForm()

    data = {
        'form': form,
        'error': erorr
    }
    return render(req, 'news/create.html', data)
