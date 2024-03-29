from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import RequestLog
from videocreator.creator import create_running_text_video
# Create your views here.


def index(request):
    return render(request, 'video/index.html')


def run_text(request):
    text = request.GET.get('text', '')
    log = RequestLog(text=text, date=timezone.now())
    log.save()
    if text:
        # Создаем видео с текстом
        duration = 4  # длительность видео в секундах
        video_path = "media/my_video.mp4"
        create_running_text_video(text, video_path, duration)
        # Отправляем видео пользователю
        with open(video_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return response
    return redirect('index')