from rest_framework import routers
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='Post')
router.register(r'groups', GroupViewSet, basename='Group')
router.register(r'follow', FollowViewSet, basename='Follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
