from django.urls import path
from .views import ( add_book , view_book , delete_book , update_book )

urlpatterns = [
    path('add_book/',add_book,name='Add_Book'),
    path('view_book/',view_book,name='View_Book'),
    path('update_book/<int:pk>/',update_book,name='Update_Book'),
    path('delete_book/<int:pk>/',delete_book,name='Delete_Book')
]