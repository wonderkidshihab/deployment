from abc import update_abstractmethods
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='images/',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='blogs', null=True)
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    
    def __str__(self):
        return self.comment[0:50]

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='images/',)
    isAndroidApp = models.BooleanField(default=False)
    isIOSApp = models.BooleanField(default=False)
    isFlutterApp = models.BooleanField(default=False)
    isWebsite = models.BooleanField(default=False)
    playStoreLink = models.URLField(null=True)
    appStoreLink = models.URLField(null=True)
    websiteLink = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey('PortfolioCategory', on_delete=models.CASCADE, related_name='portfolios', null=True)
    def __str__(self):
        return self.title
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name