from django.urls import path
from .views import book_list, book_detail, pdf_view

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('<int:book_id>/pdf/', pdf_view, name='book_detail'),
]
