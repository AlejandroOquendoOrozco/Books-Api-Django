from django.contrib import admin
from django.urls import path
from LibrosApi.views import books_list,book_create,book
urlpatterns = [
   path('',book_create),
   path('list/',books_list),
   path('<int:pk>',book)
]
