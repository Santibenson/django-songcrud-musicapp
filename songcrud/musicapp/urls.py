from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'artistes', ArtisteViewSet, basename='artistes')
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'lyrics', LyricViewSet, basename='lyrics')
urlpatterns = [] + router.urls