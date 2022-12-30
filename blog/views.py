from datetime import datetime

from django.shortcuts import render, redirect
from blog.forms import SignUpForm, BlogPostForm

# Create your views here.

from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    title = 'xxx'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    # def get(self, request):
    #     return HttpResponse(f'<h1>Ceci est ma page {self.title} </h1>')


def accounts(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign-up.html', context)


def blog_post(resuest):
    if resuest.method == 'POST':
        form = BlogPostForm(resuest.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('blog')
    else:
        init_values = {}
        if resuest.user.is_authenticated:
            init_values['author'] = resuest.user
        init_values['date'] = datetime.today()
        form = BlogPostForm(initial=init_values)
    context = {
        'form': form,
    }
    return render(resuest, 'accounts/sign-up.html', context)
