# start_debug.py
import sys
import traceback

try:
    import uvicorn
    import os
    from pathlib import Path

    # Определяем базовую директорию
    if getattr(sys, 'frozen', False):
        BASE_DIR = Path(sys._MEIPASS)
    else:
        BASE_DIR = Path(__file__).parent

    os.chdir(BASE_DIR)

    print("===========================================")
    print("   Programming Wiki - Запуск сервера")
    print("===========================================")
    print(f"Базовая директория: {BASE_DIR}")
    print(f"Текущая директория: {os.getcwd()}")
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

except Exception as e:
    print("\n" + "="*50)
    print("ОШИБКА ПРИ ЗАПУСКЕ:")
    print("="*50)
    traceback.print_exc()
    print("="*50)
    input("\nНажмите Enter для выхода...")
    sys.exit(1)