from .views import cities, CityDetailView
from django.urls import path

app_name = 'cities'

urlpatterns = [
    path('', cities, name = 'cities'),
    path('<int:pk>/', CityDetailView.as_view(), name = 'detail'),    #<int:pk> означает что тут целое число которое будет переведено в pk
]

