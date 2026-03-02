from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    isbn_no = models.CharField(max_length=13,unique=True)
    published_date = models.DateField()
    price = models.DecimalField(decimal_places=2,max_digits=8)
    pages = models.IntegerField()
    language = models.CharField(max_length=100)
    isAvailable = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)