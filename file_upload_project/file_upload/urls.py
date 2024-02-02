from django.urls import path, include
from .views import FileUploadViewSet, FileListViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

router.register(prefix="upload", viewset=FileUploadViewSet, basename="upload")
router.register(prefix="file", viewset=FileListViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
