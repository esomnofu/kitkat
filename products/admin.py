from django.contrib import admin
from .models import Product, News, Ratings

admin.site.register(Ratings)
admin.site.register(Product)
admin.site.register(News)