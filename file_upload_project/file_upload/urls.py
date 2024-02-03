from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FileListViewSet, FileUploadViewSet

app_name = 'api'

router = DefaultRouter()

router.register(prefix="upload", viewset=FileUploadViewSet, basename="upload")
router.register(prefix="file", viewset=FileListViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
