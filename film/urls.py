from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'film'
urlpatterns = [
    path("anime1/", views.AnimeView.as_view(), name='Naruto'),
]