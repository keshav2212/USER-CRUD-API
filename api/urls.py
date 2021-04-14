from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('',views.home.as_view()),
    path('apifun',views.apifun.as_view()),
 	path('apifun/<int:pk>',views.apifun.as_view()),
       
]
