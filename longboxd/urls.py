"""longboxd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from longboxdapi.models.publisher import Publisher
from longboxdapi.models.team import Team
from longboxdapi.views import register_user, login_user, ComicTypeView
from longboxdapi.views import ComicView
from longboxdapi.views import CollectorView
from longboxdapi.views import CreatorView
from longboxdapi.views.character import CharacterView
from longboxdapi.views.publisher import PublisherView
from longboxdapi.views.team import TeamView
from longboxdapi.views.user_review import ReviewView



router = routers.DefaultRouter(trailing_slash=False)
router.register(r'comictypes', ComicTypeView, 'comictype')
router.register(r'comics', ComicView, 'comic')
router.register(r'collectors', CollectorView, 'collector')
router.register(r'creators', CreatorView, 'creator')
router.register(r'characters', CharacterView, 'character')
router.register(r'publishers', PublisherView, 'publisher')
router.register(r'teams', TeamView, 'teams')
router.register(r'reviews', ReviewView, 'review')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
