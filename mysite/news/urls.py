from .views import get_category, \
    new_detail, add_news, NewsList, \
    NewsByCategory, ViewNews, CreateNewsView, test
from django.urls import path

urlpatterns = [
    # path('', index, name='index'),
    path('', NewsList.as_view(), name='index'),
    # path('category/<int:category_id>/', get_category, name='category-id'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category-id'),
    # path('news/<int:news_id>/', new_detail, name='new-detail'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='new-detail'),
    # path('news/add-new/', add_news, name='add-news')
    path('news/add-new/', CreateNewsView.as_view(), name='add-news'),
    path('test/', test)
    ]
