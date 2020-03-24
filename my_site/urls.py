from django.contrib import admin
from django.urls import path, include
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('publishers/', views.publishers),
    path('p_library/', include('p_library.urls', namespace='p_library')),
]