from .views import CustomUserViewSet
from django.urls import path
from djoser import views as djoser_views

urlpatterns =[
    path('auth/users/me/', CustomUserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put':'update', 'delete':'destroy'}), name='user'),
]