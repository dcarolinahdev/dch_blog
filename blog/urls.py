from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('post/new/', views.post_new, name='post_new'),
    path("post/<int:pk>/", views.DetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path("drafts/", views.DraftView.as_view(), name="post_draft_list"),
]