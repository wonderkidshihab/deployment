from rest_framework import serializers, generics
from .models import *

class BlogSerializer(generics.ListAPIView):
    queryset = Blog.objects.all()
    class Meta:
        model = Blog
        fields = '__all__'
        
class BlogDetailSerializer(generics.RetrieveAPIView):
    class Meta:
        model = Blog
        fields = '__all__'
class CategorySerializer(generics.ListAPIView):
    class Meta:
        model = Category
        fields = '__all__'

class CommentByBlogSerializer(generics.ListAPIView):
    class Meta:
        model = Comment
        fields = '__all__'
    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)
class PortfolioSerializer(generics.ListAPIView):
    class Meta:
        model = Portfolio
        fields = '__all__'
class PortfolioDetailSerializer(generics.RetrieveAPIView):
    class Meta:
        model = Portfolio
        fields = '__all__'
class PortfolioCategorySerializer(generics.ListAPIView):
    class Meta:
        model = PortfolioCategory
        fields = '__all__'
class PortfolioByCategorySerializer(generics.ListAPIView):
    class Meta:
        model = Portfolio
        fields = '__all__'
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Portfolio.objects.filter(Category_id=category_id)
class CommentSerializer(generics.ListAPIView):
    class Meta:
        model = Comment
        fields = '__all__'
class CommentDetailSerializer(generics.RetrieveAPIView):
    class Meta:
        model = Comment
        fields = '__all__'
        
class CreateCommentByBlogSerializer(generics.CreateAPIView):
    class Meta:
        model = Comment
        fields = '__all__'
    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        serializer.save(blog_id=blog_id)
        


        

