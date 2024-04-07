from django.urls import path
from .views import artist_detail, artist_list, home

urlpatterns = [
    path('artists/', artist_list, name='artist_list'),
    path('', home, name='home'),
    path('artists/<int:pk>/', artist_detail, name='artist_detail'),

]
