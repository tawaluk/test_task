from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):

    def validate_file(self, file):
        
        if file.size > 100000000:  # Пример: ограничение размера файла до 100 МБ
            raise serializers.ValidationError("File size should not exceed 100 MB.")
        return file

    class Meta:

        model = File
        fields = ("id", "file", "uploaded_at", "processed")
