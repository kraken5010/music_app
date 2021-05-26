from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', PoisonHome.as_view(), name='home'),
    path('news/', PoisonNews.as_view(), name='news'),
    path('media/', PoisonAlbum.as_view(), name='media'),
    path('gallery/<slug:album_slug>', PoisonGallery.as_view(), name='gallery'),
    path('tours/', cache_page(60)(PoisonTour.as_view()), name='tours'),
    path('connect/', ConnectForm.as_view(), name='connect'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PoisonCategory.as_view(), name='category'),
]