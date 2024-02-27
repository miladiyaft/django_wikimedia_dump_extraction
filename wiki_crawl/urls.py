from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('save_data/', views.save_data, name="save_data"),
]