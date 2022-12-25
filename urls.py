"""anime_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from reviews_movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', views.genre_list),
    path('genre/<int:pk>', views.genre_detail),
    path('movie/', views.movie_list),
    path('movie/<int:pk>', views.movie_detail),
    path('reviews/', views.reviews_list),
    path('reviews/<int:pk>', views.reviews_detail),
    path('star/', views.raitingStar_list),
    path('star/<int:pk>', views.raitingStar_detail),
    path('raiting/', views.raiting_list),
    path('raiting/<int:pk>', views.raiting_detail),
    path('auth/login/', views.aut),
    #path('api/v1/drf-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)