from django.views.generic import ListView
from forum.models import Game, Genre


class GameListView(ListView):
    template_name = 'forum/game_list.html'
    context_object_name = 'games'
    paginate_by = 12

    def get_queryset(self):
        queryset = Game.objects.all()


        genre_id = self.request.GET.get('genre')
        if genre_id:
            queryset = queryset.filter(genres=genre_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['is_paginated'] = self.get_queryset().count() > self.paginate_by
        return context
