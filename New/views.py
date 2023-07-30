from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,ListView
from .models import NewList, Category
from .forms import ContactForm
# from .models import Blog

# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = NewList.objects.all().order_by('-published_time')[:5]
#     local_one = NewList.objects.filter(category__name='Mahalliy').order_by('-published_time')[:1]
#     local_news = NewList.published.all().filter(category__name='Mahalliy').order_by('-published_time')[1:6]
#     context = {
#         "news_list" : news_list,
#         "categories": categories,
#         "local_one": local_one,
#         'local_news': local_news,
#     }
#     return render(request, 'index.html', context)
class HomePageView(ListView):
    model = NewList
    template_name = 'index.html'
    context_object_name = 'NewList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.model.objects.all()
        context['news_list'] = NewList.objects.all().order_by('-published_time')[:5]
        context['local_one'] = NewList.objects.filter(category__name='Mahalliy').order_by('-published_time')[:1]
        context['local_news'] = NewList.published.all().filter(category__name='Mahalliy').order_by('-published_time')[1:6]
        context['xorij_news'] = NewList.published.all().filter(category__name='Xorij').order_by('-published_time')[1:6]
        context['texno_news'] = NewList.published.all().filter(category__name='Texno').order_by('-published_time')[:6]
        context['sport_news'] = NewList.published.all().filter(category__name='Sport').order_by('-published_time')[1:6]

        return context

    def get_absolute_url(self):
        return reverse("single_page", args=[self,slug])

class LocalNewsView(ListView):
    model = NewList
    template_name = 'LocalNews.html'
    context_object_name = 'LocalNews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name=Mahalliy)
        return news

class TexnoNewsView(ListView):
    model = NewList
    template_name = 'TexnoNews.html'
    context_object_name = 'TexnoNews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name=Texno)
        return news

class XorijNewsView(ListView):
    model = NewList
    template_name = 'XorijNews.html'
    context_object_name = 'XorijNews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name=Xorij)
        return news

class SportNewsView(ListView):
    model = NewList
    template_name = 'SportNews.html'
    context_object_name = 'SportNews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name=Sport)
        return news

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }

        return render(request, 'contact.html', context)

    def post(self, request,*args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langanligiz uchun tashakkur!</h2>")
        context = {
            "form": form,
        }
        return render(request, 'contact.html', context)

def news_list(request):
    # news_list = NewList.objects.all()     #barcha postlarni chiqaradi
    # news_list = NewList.published.all()   #bu hammasini managers orqali chiqaradi
    news_list = NewList.objects.filter(status=NewList.Status.Published)[:6]    #filter orqali publish qilinganlarni chiqarish
    context = {
        "news_list": news_list
    }

    return render(request, 'news_list.html', context)

def news_detail(request, news):
    news_list = get_object_or_404(NewList, slug=news, status=NewList.Status.Published)
    context = {
        "news_list": news_list,
    }
    return render(request, 'single_page.html', context)


####  funksiya orqali ContactPageView ####
# def ContactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("index.html")
#     context = {
#         "form": form,
#     }
#     return render(request, 'contact.html', context)

   
##################################
### Funksiyaga asoslangan view ###
##################################
# def BlogListView(request):
#     blogs = Blog.objects.all()
#     users = User.objects.all()
#     context = {
#         "blogs": blogs,
#         "users": users,
#     }

#     return render(request, 'home.html', context=context)

# ################################################
# ### Http404 orqali try except qilib yozilgan ###
# ################################################
# # def BlogDetailView(request, id):
# #     try:
# #         blog = Blog.objects.get(id=id)        
# #         context = {
# #             "blog": blog,
# #         }
# #     except Blog.DoesNotExsit:
# #         raise Http404("No blog found")

# #     return render(request, 'blog_detail.html', context=context)

# def BlogDetailView(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     context = {
#             "blog": blog,
#         }

#     return render(request, 'blog_detail.html', context=context)

###################################
### class larga asoslangan view ###
###################################

# class BlogListView(ListView):
#     model = Blog
#     template_name = 'home.html'
#     context_object_name = "blogs"

# class BlogDetailView(DetailView):
#     model = NewList
#     template_name = 'news_detail.html'
