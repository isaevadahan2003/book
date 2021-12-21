from django.views.generic import ListView
from . import models
from django.urls import reverse, reverse_lazy

class AnimeView(ListView):
    queryset = models.Anime.objects.all()
    context_object_name = 'object_list'
    template_name = 'anime1/anime_list.html'
