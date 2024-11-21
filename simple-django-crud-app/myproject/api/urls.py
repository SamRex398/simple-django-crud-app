from django.urls import path
from . import views

urlpatterns = [
    path('note/create', views.createNote, name='Create Note'),
    path('notes/', views.get_notes, name='Get Notes'),
    path('note/<int:pk>', views.note_details, name='Note'),

    path('user/register', views.signup, name='User'),
    path('user/login', views.login, name='User'),
]
