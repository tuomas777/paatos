from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from decisions.api import ActionViewSet, CaseViewSet, CategoryViewSet, EventViewSet, OrganizationViewSet

router = DefaultRouter()
router.register(r'action', ActionViewSet)
router.register(r'case', CategoryViewSet)
router.register(r'category', CaseViewSet)
router.register(r'event', EventViewSet)
router.register(r'organization', OrganizationViewSet)

urlpatterns = [
    url(r'^', include(router.urls, namespace='v1')),
]
