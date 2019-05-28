from django.contrib import admin
from django.urls import path, include
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]