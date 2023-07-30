from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.
########################################
### managers bilan ishlash           ###
########################################
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=NewList.Status.Published)



class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):

        return self.name

class NewList(models.Model):

    class Status(models.TextChoices):
        Draft = "DR", "Draft",
        Published = "PB", "Published",

    title = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField(upload_to='media/')
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):

        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):

        return self.email


# class Blog(models.Model):
#     title = models.CharField(max_length=150)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     text = models.TextField()

#     def __str__(self):

#         return self.title