from django.urls import path, include
from .serializers import *

urlpatterns = [
    path('blog/', BlogSerializer.as_view(), name='blog-list'),
    path('blog/<int:pk>', BlogDetailSerializer.as_view()),
]
