from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('blogs/', BlogSubmitView.as_view(), name='submit-blog'),
    path('blog-info/<uuid:pk>/', BlogInfoView.as_view(), name='blog_info'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
