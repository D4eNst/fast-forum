from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# from forum_app.models import Category, Post


class MainView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'forum/index.html', context=context)


class ActionListView(TemplateView):
    template_name = 'forum/actions.html'
