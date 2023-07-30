from .models import NewList,Category
# from .views import HomePageView

def latest_news(request):
    latest_news = NewList.published.all().order_by('-published_time')[:8]
    categories = Category.objects.all()

    context = {
        'latest_news': latest_news,
        'categories': categories,
    }
    return context