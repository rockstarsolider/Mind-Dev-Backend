from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('fazes/', CourseFazes.as_view(), name='fazes'),
    path('sections/<int:pk>', FazeSections.as_view(), name='sections'),
]

