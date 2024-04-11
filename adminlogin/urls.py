from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.profile_view, name='AdminProfile'),
    path('database/', views.database_view, name='DataView')
]