from moviepy.editor import *
import numpy as np


# Функция для создания видео с бегущей строкой текста
def create_running_text_video(text, duration, output_path):
    # Создаем функцию, которая возвращает изображение с текстом в нужной позиции
    def make_frame(t):
        # Инициализируем изображение с черным фоном
        img = np.zeros((720, 1280, 3), dtype=np.uint8)

        # Вычисляем текущую позицию текста на основе времени
        x_position = int((1280 + len(text) * 20) * t / duration)

        # Рисуем текст на изображении
        txt_clip = TextClip(text, fontsize=70, color='white', bg_color='black').set_position((x_position, 300))

        # Возвращаем изображение с текстом
        return CompositeVideoClip([txt_clip]).get_frame(t)

    # Создаем видео с помощью функции make_frame
    video = VideoClip(make_frame, duration=duration)

    # Сохраняем видео
    video.write_videofile(output_path, fps=24)


# Пример использования
text = "Это текст для бегущей строки"
duration = 10  # длительность видео в секундах
output_path = "running_text.mp4"
create_running_text_video(text, duration, output_path)

