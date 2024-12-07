from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_favorite, name='add_favorite'),
    path('remove/<int:city_id>/', views.remove_favorite, name='remove_favorite'),
]
