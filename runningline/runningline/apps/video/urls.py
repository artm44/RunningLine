from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('runtext', views.run_text, name='run_text'),
]