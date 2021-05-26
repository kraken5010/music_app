from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .models import *
from .utils import *
from .forms import *


# Отображение главной страницы
class PoisonHome(DataMixin, ListView):
    paginate_by = 4
    model = News
    template_name = 'poison/index.html'
    context_object_name = 'posts'   # переменная для отображения статей в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')
        return context | c_def

    def get_queryset(self):
        return News.objects.all().filter(is_published=True)    # выводит новости отмеч. для публикации


class PoisonCategory(DataMixin, ListView):
    model = News
    template_name = 'poison/news.html'
    context_object_name = 'posts'   # переменная для отображения статей в шаблоне
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = CategoryNews.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='News:' + str(c.name),  # в заголовке отображается категория + ее название
                                      cat_selected=c.pk)
        return context | c_def

    def get_queryset(self):     # выводит список по выбранной рубрике
        return News.objects.all().filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


# Отображение страницы новостей
class PoisonNews(DataMixin, ListView):
    model = News
    template_name = 'poison/news.html'
    context_object_name = 'posts'   # переменная для отображения статей в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='News')
        return context | c_def

    def get_queryset(self):
        return News.objects.all().filter(is_published=True).select_related('cat')    # выводит новости отмеч. для публикации


# Отображение страницы новости
class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'poison/post.html'
    slug_url_kwarg = 'post_slug'    # для использования слага в urlpatterns
    context_object_name = 'post'    # для использования post в шаблоне post.html

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return context | c_def


# Страница с Альбомами
class PoisonAlbum(DataMixin, ListView):
    model = Photo
    template_name = 'poison/media.html'
    context_object_name = 'albums'   # переменная для отображения статей в шаблоне

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Media')
        return context | c_def

    # def get_queryset(self):     # ??? выводит список по выбранной рубрике
    #     return Photo.objects.all().filter(album__slug=self.kwargs['album_slug'])


# Страница с фотографиями
class PoisonGallery(DataMixin, ListView):
    model = Photo
    template_name = 'poison/gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Album.objects.get(slug=self.kwargs['album_slug'])
        c_def = self.get_user_context(title='Gallery ' + str(c.title))
        return context | c_def


# Страница с Турами
class PoisonTour(DataMixin, ListView):
    model = Tour
    template_name = 'poison/tours.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Tours')
        return context | c_def

    def get_queryset(self):
        return News.objects.all()


# Страница обратной связи
class ConnectForm(DataMixin, FormView):
    form_class = FeedbackForm
    template_name = 'poison/connect.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Connect')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# Регистрация нового пользователя
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'poison/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign Up')
        return context | c_def

    # При успешной регистрации авторизация пользователя
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# Авторизация пользователя
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'poison/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign In')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


# Функция выхода пользователя и перенаправление на авторизацию
def logout_user(request):
    logout(request)
    return redirect('login')






