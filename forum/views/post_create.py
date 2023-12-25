from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from forum.models import Post
from forum.forms.post_form import PostForm


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum_home')
