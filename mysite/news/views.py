from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q, Count, F
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


def test(request):
    objects = News.objects.filter(is_published=True)
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class NewsList(MyMixin, ListView):
    model = News
    template_name = 'news/index_news_list.html'
    context_object_name = 'news'
    # queryset = News.objects.select_related('category')
    mixin_prop = 'hello worlds'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['categories'] = self.test()
        context['mixin_prop'] = self.get_upper('test')

        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     categories = Category.objects.all()
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'categories': categories
#     }
#     return render(request, 'news/index.html', context=context)


class NewsByCategory(MyMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index_news_list.html'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data()
        context['categories'] = self.test()
        return context


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)


def new_detail(request, news_id):
    # news = News.objects.get(pk=news_id)
    news = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/news-detail.html', context={'news': news})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    return render(request, template_name='news/add_news.html', context={'form': form})


class ViewNews(MyMixin, DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    # slug_url_kwarg = '' это для слага
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(id=self.kwargs['news_id'])


class CreateNewsView(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('index')
    raise_exception = True
    # login_url = '/admin/'


