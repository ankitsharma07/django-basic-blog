from django.urls import path

from . import views
from .views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    # path("", views.home, name="blog-home"),
    path(
        "", PostListView.as_view(), name="blog-home"
    ),  # <app>/<model>_<viewtype>.html
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
]
