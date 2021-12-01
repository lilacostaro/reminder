from django.urls import path
from . import views

urlpatterns = [
    path('', views.itemList, name='task-list'),
    path('product/<int:id>', views.listaView, name='lista-view'),
    path('newitem/', views.newItem, name='new-item'),
    path('edit/<int:id>', views.editItem, name='edit-item'),
    path('history/edit/<int:id>', views.editItem, name='edit-item'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('history/changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('delete/<int:id>', views.deleteItem, name='delete-item'),
    path('history/delete/<int:id>', views.deleteItem, name='delete-item'),
    path('history/', views.history, name='history'),
    path('dashboard/', views.dashboard, name='dashboard'),
]