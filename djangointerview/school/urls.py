
from django.urls import path
from .views import myfun

urlpatterns = [
    path('', myfun ),
]
