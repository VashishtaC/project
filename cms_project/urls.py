from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cms_app.views import UserViewSet, PostViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')),  # Authentication URLs
    path('api/auth/registration/', include('rest_auth.registration.urls')),  # Registration URLs
]
