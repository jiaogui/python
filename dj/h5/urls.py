from django.urls import path, include

import h5.views

urlpatterns = [
    path('index', h5.views.index),
]