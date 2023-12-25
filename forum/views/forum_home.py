from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import View
from forum.models import Genre, Post


class ForumHomeView(View):
    template_name = 'forum/forum_home.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.all()

        genre_id = self.request.GET.get('genre')
        if genre_id:
            queryset = queryset.filter(game__genres__id=genre_id)

        return queryset

    def get(self, request):
        genres = Genre.objects.all()
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
            'genres': genres,
            'is_paginated': self.get_queryset().count() > self.paginate_by,
            'page_obj': page_obj,
            'paginator': paginator,
            'posts': posts
        }

        return render(request, self.template_name, context)
