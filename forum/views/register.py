from django.urls import reverse_lazy
from django.views.generic import CreateView

from forum.forms.register_form import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'forum/register.html'

    def get_success_url(self):
        return reverse_lazy('login')
