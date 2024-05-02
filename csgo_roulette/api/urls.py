from django.urls import path
from .views import GetWeapons

urlpatterns = [
    path('weapons',GetWeapons.as_view())
]
