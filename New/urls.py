from django.urls import path
from django.http import HttpResponse
# from .views import BlogListView,BlogDetailView
from .views import news_list, news_detail
from New.views import HomePageView, ContactPageView, \
    LocalNewsView,SportNewsView,XorijNewsView,TexnoNewsView

urlpatterns = [
    ### funksiya orqali qilingan url ###    news_list,
    # path('', BlogListView, name='home_page'),
    # path('<int:id>/', BlogDetailView, name='detail_page'),
    ### class orqali qilingan url ###
    # path("", BlogListView.as_view(), name="home_page"),
    # path("<int:pk>/", BlogDetailView.as_view(), name="detail_page"),
    #### 127.0.0.1:8000/news/all/  link orqali kiriladi  ####
    path('all/', news_list, name='list_page'),
    path('<slug:news>/', news_detail, name='single_page'),
    path('', HomePageView.as_view(), name='home_page'),
    # path('contact/', ContactPageView, name='contact_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('texno/',TexnoNewsView.as_view(), name='texno_news_page'),
    path('xorij/', XorijNewsView.as_view(), name='xorij_news_page'),
]