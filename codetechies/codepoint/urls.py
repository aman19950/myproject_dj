
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="home"),
    path('course/<str:slug>/', views.course_informations, name="cour"),
    path('course1/<str:slug>/', views.testing_de, name="cour1"),
]
