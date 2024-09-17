from django.urls import path,include,re_path
from . views import helloView,addbookView,addBook,editBookView,editBook,deleteBookView
from django.contrib import admin


urlpatterns = [
   path('', helloView),
   path('add-book/',addbookView),
   path('add-book/add',addBook),
   path("edit-book",editBookView),
   path("edit-book/edit",editBook),
   path("delete-book",deleteBookView)
]