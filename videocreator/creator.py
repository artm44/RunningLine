import cv2
import numpy as np


# Функция для создания видео с бегущей строкой текста
def create_running_text_video(text: str, output_path: str, duration: int = 4):
    # Создаем видео запись
    width, height = 80, 80
    fps = 24
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Инициализируем начальные параметры для бегущей строки
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 2
    font_thickness = 2
    text_width, text_height = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    offset = (height - text_height) // 2
    y_position = height - offset
    background_colour = [125, 30, 80]  # Цвет фона

    # Создаем видео
    for t in np.linspace(0, duration, int(duration * fps)):
        frame = np.full((height, width, 3), background_colour, dtype=np.uint8)

        # Вычисляем текущую позицию текста на основе времени
        x_position = width // 2 - int(text_width * t / duration)

        # Рисуем текст на кадре
        cv2.putText(frame, text, (x_position, y_position), font, font_scale, (255, 255, 255), font_thickness)

        # Добавляем кадр в видео запись
        out.write(frame)

    # Закрываем видео запись
    out.release()


def main():
    # Пример использования
    text = input('Введите текст\n')
    duration = 4  # длительность видео в секундах
    output_path = "../videos/my_video.mp4"
    create_running_text_video(text, output_path, duration)


if __name__ == '__main__':
    main()
