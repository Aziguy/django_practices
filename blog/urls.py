from django.urls import path, include
from . import views
from .views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(title='Accueil du site'), name='home'),
    path('about/', HomeView.as_view(title='about'), name='about'),
    # path('', views.accounts, name='accounts'),
    path('index/', views.blog_post, name='blog'),
]
