from django.shortcuts import render
from rest_framework.views import APIView
from .serilaizers import *
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework import generics
# Create your views here.


class BlogSubmitView(generics.CreateAPIView):
    serializer_class = BlogSubmitSerializer

    def create(self, request, *args, **kwargs):

        # Pass additional parameters to the serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BlogInfoView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer