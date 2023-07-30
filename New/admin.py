from django.contrib import admin
from .models import NewList, Category, Contact
### dastlabki darslar uchun ###
# from .models import Blog
# Register your models here.
# admin.site.register(Blog)

@admin.register(NewList)
class NewListAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'slug', 'published_time','status']
    list_filter = ['status', 'created_time', 'published_time']
    prepopulated_fields = {"slug":('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title','text']
    ordering = ['status', 'published_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Contact)