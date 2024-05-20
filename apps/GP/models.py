from django.db import models
import uuid
# Create your models here.
class Audio_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique identifier for this Audio, generated automatically.")
    Audio = models.FileField(upload_to='Audios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)