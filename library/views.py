from django.shortcuts import render
# from django.views.generic import ListView
from rest_framework import generics,permissions

from .models import Books
from .serializer import BookSerializer

#for html templet view
# class BooksListView(ListView):
#     model = Books
#     template_name = "Books_list.html"

class BooksListView(generics.ListAPIView):
    permission_classes =(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer



# Create your views here.
