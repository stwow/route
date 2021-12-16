from .views import TrainView, TrainDetailView,TrainCreateView,TrainUpdateView,TrainDeleteView
from django.urls import path

app_name = 'trains'

urlpatterns = [
    path('', TrainView.as_view(), name = 'trains'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    # <int:pk> означает что тут целое число которое будет переведено в pk
    path('add/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),

]

