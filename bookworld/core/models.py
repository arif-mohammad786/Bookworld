from django.db import models

# Create your models here.

#Model for book category
class book_category(models.Model):
    category=models.CharField(max_length=70)

# Model for books
class available_book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.IntegerField()
    image=models.FileField()


# Model to store information of customers 
class buy_book_model(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    address=models.TextField()

