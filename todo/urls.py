from django.urls import path, include

from . import views

app_name = 'todo'

urlpatterns = [
    
    path('', views.list, name="list"),
    path('add/', views.add_todo_view, name="add-todo"),
    path('update-todo/<int:pk>/', views.update_todo_view, name='update_todo'),
    path('delete-todo/<int:pk>/', views.delete_todo_view, name='delete_todo'),
]