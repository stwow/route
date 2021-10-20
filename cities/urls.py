from .views import index
from django.urls import path

app_name = 'cities'

urlpatterns = [
    path('', index, name = 'index'),
]

