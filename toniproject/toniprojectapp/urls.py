from . import views
from django.urls import path

from django.contrib import admin




urlpatterns = [

      path('',views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path("contact",views.contact,name='contact')
    # path('', views.addition, name="addition"),
    # path('add/',views.result,name='result')
]