from django.db import models

# Create your models here.
class Transcription(models.Model):
        id = models.AutoField(primary_key=True, auto_created=True)
        path = models.CharField(max_length=200)
        created_at = models.DateTimeField(auto_now_add=True)
        progress = models.IntegerField(default=0)
        status = models.IntegerField(default=0) # 0 created  1 transcribing 2 completed