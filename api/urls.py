from django.urls import path
from .views import artist_details
urlpatterns = [
    # path('view_saves/'),
    path('search_artist/<str:artist_name>', artist_details, name='artist_details')
]
