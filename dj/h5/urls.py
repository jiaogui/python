from django.urls import path, include

import h5.views

app_name = 'html5'

urlpatterns = [
    path('index', h5.views.index),
    path('userLists', h5.views.userLists, name='userLists'),
    path('indexCreate', h5.views.indexCreate),
]