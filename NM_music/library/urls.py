from django.urls import path
from .views import artist_list

urlpatterns = [
    path('artists/', artist_list, name='artist_list'),
]
