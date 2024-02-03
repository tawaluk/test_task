from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadViewSet(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.save()
        file_obj_id: str = file.id
        process_file.delay(file_obj_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileListViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer
