from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='./')
    sha256 = models.CharField(max_length=256)
    uploaded_count = models.IntegerField(default=1)

    def filepath(self):
        return self.document.path
