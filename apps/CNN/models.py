from django.db import models
import uuid
# Create your models here.
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique identifier for this image, generated automatically.")
    picture = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)