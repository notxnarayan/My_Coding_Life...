from django.contrib import admin
from django.urls import path
from T1 import views
urlpatterns = [

    path('', views.landingpage,name='main'),

]