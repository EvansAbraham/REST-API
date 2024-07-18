from django.urls import path
from home.views import BlogViews, PublicBlog

urlpatterns = [
    path('blogs/', BlogViews.as_view()),
    path('', PublicBlog.as_view())
]
