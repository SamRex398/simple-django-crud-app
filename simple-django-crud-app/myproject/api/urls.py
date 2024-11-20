from django.urls import path
from . import views

urlpatterns = [
    path('note/create', views.createNote, name='Create Note'),
    path('notes/', views.getNotes, name='Get Notes'),
    path('note/<int:pk>', views.noteDetails, name='Note'),
]
