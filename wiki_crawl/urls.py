from django.urls import path
from .views import ParseAndSaveView


urlpatterns = [
    path('save_data/', ParseAndSaveView.as_view(), name="save_data"),
]