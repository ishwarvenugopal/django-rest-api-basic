from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sample', views.SampleProtectedView.as_view())
]
