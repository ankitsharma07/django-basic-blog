from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from blog.models import Post

posts = [
    {
        "author": "Ankit Sharma",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "Feb 1, 2022",
    },
    {
        "author": "Corey S.",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "Jan 31, 2022",
    },
]

# Create your views here.
def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]  # newest to oldest (by adding -)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
