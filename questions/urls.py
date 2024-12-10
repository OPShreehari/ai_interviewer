from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('add/', views.add_question, name='add_question'),
    path('editor/', views.editor, name='editor'),
    path('execute_code/', views.execute_code, name='execute_code'),
]
