from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('details/<id>', views.details, name='details'),
    path('submit/', views.submit, name='submit'),
    path('delete/<id>', views.delete, name='delete')
]