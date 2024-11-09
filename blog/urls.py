from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("drafts/", views.DraftView.as_view(), name="post_draft_list"),
]