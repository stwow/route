from .views import cities, CityDetailView,CityCreateView, CityUpdateView,CityDeleteView,CityView
from django.urls import path

app_name = 'cities'

urlpatterns = [
    # path('', cities, name = 'cities'),
    path('', CityView.as_view(), name = 'cities'),
    path('<int:pk>/', CityDetailView.as_view(), name = 'detail'),    #<int:pk> означает что тут целое число которое будет переведено в pk
    path('add/', CityCreateView.as_view(), name ='create' ),
    path('update/<int:pk>/',  CityUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/',  CityDeleteView.as_view(), name = 'delete'),
]