from django.contrib import admin
from .models import Blog, Category, Comment, Portfolio, PortfolioCategory

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Portfolio)
admin.site.register(PortfolioCategory)
