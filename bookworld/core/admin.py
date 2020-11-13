from django.contrib import admin
from .models import book_category,available_book,buy_book_model
# Register your models here.
@admin.register(book_category)
class book_category_admin(admin.ModelAdmin):
    list_display=('id','category')

@admin.register(available_book)
class admin_available_book(admin.ModelAdmin):
    list_display=('id','title','author','publisher','category','price','image')


@admin.register(buy_book_model)
class admin_buy_book(admin.ModelAdmin):
    list_display=('id','title','author','publisher','category','name','phone','address')