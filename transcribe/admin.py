from django.contrib import admin
from .models import Transcription
# Register your models here.

@admin.register(Transcription)
class TranscriptionAdmin(admin.ModelAdmin):
    # fields = ["path"]
    def status(obj):
        if obj.status == 0:
            return "Queue"
        elif obj.status == 1:
            return "Transcribing"
        elif obj.status == 2:
            return "Completed"
    def transcription_progress(obj):
        return f"{obj.progress}%"
    list_display = ['path', status, transcription_progress]