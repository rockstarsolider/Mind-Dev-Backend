from django.urls import path, include
from djoser import views as djoser_views
from .views import UserViewSet, UserCreateView, StudentViewSet, UploadCV
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')

urlpatterns =[
    path('auth/users/me/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put':'update', 'delete':'destroy'}), name='user'),
    path('auth/users/', UserCreateView.as_view(), name='user'),
    path('auth/student/', StudentViewSet.as_view({'get': 'retrieve'}), name='user'),
    path('auth/student/<int:pk>/', StudentViewSet.as_view({'patch':'partial_update'})),
    path('auth/student/cv/<int:pk>/', UploadCV.as_view(), name='upload-cv'),
]