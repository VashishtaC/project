from django.urls import re_path, path, include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, LikeViewSet, register_user
from . import views  # Import your views module here

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    re_path(r'^some-pattern/$', views.some_view, name='some-view'),
    path('api/', include(router.urls)),
    path('api/register/', register_user),
]
