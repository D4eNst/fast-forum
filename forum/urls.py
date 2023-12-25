from django.urls import path
import forum.views as views

urlpatterns = [
    path('', views.MainView.as_view(), name='main_page'),
    path('actions/', views.ActionListView.as_view(), name='action_list'),
    path('games/', views.GameListView.as_view(), name='game_list'),
    path('games/create/', views.GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game_detail'),
    path('forum/', views.ForumHomeView.as_view(), name='forum_home'),
    path('forum/create/', views.CreatePostView.as_view(), name='post_create'),
    path('forum/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='log-out'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
