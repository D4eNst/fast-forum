from django.views.generic.detail import DetailView
from forum.models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = 'forum/game_detail.html'  # Имя вашего шаблона для страницы с игрой
    context_object_name = 'game'  # Имя переменной контекста для доступа к объекту Game в шаблоне
