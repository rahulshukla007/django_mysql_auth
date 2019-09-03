from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('show/', views.show, name='Show'),
    path('edit/<int:id>', views.edit, name='Edit'),
    path('update/<int:id>', views.update, name='Update'),
    path('delete/<int:id>', views.delete, name='Delete'),
    path('admin/', views.adminLogin, name="Admin"),
    path('logout/', views.logOut, name='Logout')
]
