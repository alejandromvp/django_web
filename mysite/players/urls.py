from django.urls import path
from . import views

urlpatterns = [
    path('ranking1', views.post_ranking1, name='post_ranking1'),
    path('edit_ranking', views.editar_ranking, name='editar_ranking')
]