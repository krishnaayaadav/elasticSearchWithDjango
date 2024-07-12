
from django.urls import path

from .views import BlogSearchview

urlpatterns = [

    path('search-page/', BlogSearchview.as_view(), name='blog_search'),
]