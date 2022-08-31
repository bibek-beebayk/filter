from django.contrib import admin
from django.urls import path, include

from main import api as main_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('video', main_api.VideoViewSet, basename='video')
router.register('filter', main_api.FilterViewSet, basename='filter')
router.register('select', main_api.FilterSelectViewSet, basename='select')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),    
]

