from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views
from . import views as app
from django.contrib import admin

urlpatterns = [

    path('palavra', app.CadastrarPalavra.as_view(), name='cadas_palavra'),

]