from django.contrib import admin
from django.urls import path, include
from routes.views import home, find_routes


urlpatterns = [
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls')),
    path('trains/', include('trains.urls')),  #include(('trains.urls','trains')) - у него так было написано, впервые вижу
]
