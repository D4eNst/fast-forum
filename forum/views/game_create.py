from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from forum.forms.game_form import GameForm
from forum.models import Game


class GameCreateView(CreateView):
    model = Game
    template_name = 'forum/game_create.html'
    form_class = GameForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Передача формы в контекст
        return context

    def form_valid(self, form):
        # Дополнительные действия при валидной форме, если необходимо
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game_detail', kwargs={'pk': self.object.id})
