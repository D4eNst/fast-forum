from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import redirect

from forum.forms.login_form import LoginForm


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'forum/login.html'
    redirect_authenticated_user = False

    # def get_success_url(self):
    #     current_path = self.request.GET.get('next')
    #     if current_path:
    #         return reverse_lazy('main-page')


def logout_user(request):
    logout(request)
    return redirect('login')
