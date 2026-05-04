# start.py
import uvicorn
import sys
import os
from pathlib import Path

# Определяем базовую директорию
if getattr(sys, 'frozen', False):
    # Запущено из .exe
    BASE_DIR = Path(sys._MEIPASS)
else:
    # Запущено из исходников
    BASE_DIR = Path(__file__).parent

# Меняем рабочую директорию
os.chdir(BASE_DIR)

if __name__ == "__main__":
    print("===========================================")
    print("   Programming Wiki - Запуск сервера")
    print("===========================================")
    print("")
    print("Сервер запускается на http://127.0.0.1:8000")
    print("")
    print("Откройте браузер и перейдите по адресу:")
    print("  http://127.0.0.1:8000")
    print("")
    print("Для остановки нажмите Ctrl+C")
    print("===========================================")
    print("")
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )