from django.contrib import admin
from django.urls import path
from api.views import home
urlpatterns = [
    path('',home.as_view()),
]
