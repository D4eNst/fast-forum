from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from forum.models import Post, Review


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(game=self.object.game)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        text = request.POST.get('text')

        if text:
            Review.objects.create(game=post.game, user=request.user, text=text)

        return redirect('post_detail', post.id)


class AddReviewView(View):
    login_url = '/login/'  # При необходимости измените URL для редиректа на страницу входа


