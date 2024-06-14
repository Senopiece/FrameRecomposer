#### Установка и настройка
1. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
   ```

#### Использование
Программа поддерживает два режима: извлечение кадров из видео и создание видео из кадров.

1. **Извлечение кадров из видео**
   ```bash
   python FrameRecomposer.py extract --video path/to/video.mp4 --frames_dir path/to/frames_dir
   ```
   - `--video`: Путь к входному видеофайлу.
   - `--frames_dir`: Директория для сохранения извлеченных кадров.

2. **Создание видео из кадров**
   ```bash
   python FrameRecomposer.py create --frames_dir path/to/frames_dir --output path/to/output_video.mp4 --fps 30
   ```
   - `--frames_dir`: Директория, содержащая кадры.
   - `--output`: Путь для сохранения выходного видеофайла.
   - `--fps`: Количество кадров в секунду для выходного видео (по умолчанию 30).