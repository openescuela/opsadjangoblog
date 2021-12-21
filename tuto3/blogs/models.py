from django.db import models
from django.urls import reverse
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
