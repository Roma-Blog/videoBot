import yt_dlp

def download_video(url):
    """Синхронная функция для скачивания видео"""
    ydl_opts = {
        'format': 'best',
        'cookiefile': 'cookies.txt',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Загрузка завершена для: {url}")
    except Exception as e:
        print(f"Произошла ошибка при загрузке {url}: {e}")