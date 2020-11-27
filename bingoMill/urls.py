from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('museum/', views.museum, name='museum'),
    path('museum/<int:bingo_id>', views.detail, name='detail'),
]

app_name = 'bingoMill'
