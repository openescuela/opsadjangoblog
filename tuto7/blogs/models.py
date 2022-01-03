from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    resume = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='project_category')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='project_client')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogs:project_content', args=[self.id, self.category, self.client])

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField()
    job = models.CharField(max_length=50, default='?')
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    linkedin_url = models.URLField()

    def __str__(self):
        return self.last_name

class Post(models.Model):
    STATUS_CHOICES = (
                ('draft', 'Draft'),
                ('published', 'Published'), )
    title = models.CharField(max_length=100)
    image = models.ImageField()
    resume = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail', args=[self.slug, self.publish.year, self.publish.month, self.publish.day])
