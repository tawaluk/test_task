from django.db import models
from django.core.exceptions import ValidationError


class File(models.Model):

    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:

        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = ['file','uploaded_at', 'processed']


    def clean(self):

        if self.file.size > 100000000:
            raise ValidationError("File size should not exceed 100 MB.")