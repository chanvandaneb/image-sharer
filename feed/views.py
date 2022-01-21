from django.contrib import messages
from django.http import request
from django.views.generic import TemplateView, DetailView, FormView

from .forms import PostForm
from .models import Post

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')

        return context


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post


class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)



    def form_valid(self, form):
        # print("This is valid form")
        # print(form.cleaned_data['text'])
        new_object = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'You are success upload photo!')
        return super().form_valid(form)