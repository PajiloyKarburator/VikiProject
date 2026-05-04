# locustfile.py
from locust import HttpUser, task, between
import random


class ProgrammingWikiUser(HttpUser):
    """
    Имитация поведения реального пользователя сайта.
    """
    
    # Время ожидания между запросами (от 1 до 5 секунд)
    wait_time = between(1, 5)
    
    # Список ID языков и библиотек для тестирования
    language_ids = ["python", "javascript", "cpp", "java", "rust"]
    library_ids = ["django", "react", "spring", "tokio", "qt"]
    
    def on_start(self):
        """Выполняется один раз при старте пользователя."""
        print(f"Новый пользователь начал работу")
    
    @task(10)  # Вес задачи: 10 (выполняется чаще других)
    def view_home(self):
        """Просмотр главной страницы."""
        self.client.get("/", name="Главная страница")
    
    @task(8)
    def view_languages_list(self):
        """Просмотр списка языков."""
        self.client.get("/languages", name="Список языков")
    
    @task(5)
    def view_language_detail(self):
        """Просмотр детальной страницы случайного языка."""
        lang_id = random.choice(self.language_ids)
        self.client.get(f"/language/{lang_id}", name="Страница языка")
    
    @task(6)
    def view_libraries_list(self):
        """Просмотр списка библиотек."""
        self.client.get("/libraries", name="Список библиотек")
    
    @task(4)
    def view_library_detail(self):
        """Просмотр детальной страницы случайной библиотеки."""
        lib_id = random.choice(self.library_ids)
        self.client.get(f"/library/{lib_id}", name="Страница библиотеки")
    
    @task(7)
    def view_catalog(self):
        """Просмотр каталога."""
        self.client.get("/catalog", name="Каталог")
    
    @task(3)
    def search(self):
        """Поиск с различными запросами."""
        queries = ["python", "java", "react", "rust", "web"]
        query = random.choice(queries)
        self.client.get(f"/search?q={query}", name="Поиск")
    
    @task(2)
    def filter_languages(self):
        """Фильтрация языков по типизации."""
        typing = random.choice(["Статическая", "Динамическая"])
        self.client.get(f"/languages?typing={typing}", name="Фильтр языков")
    
    @task(2)
    def filter_catalog(self):
        """Фильтрация каталога."""
        filter_type = random.choice(["languages", "libraries"])
        self.client.get(f"/catalog?type={filter_type}", name="Фильтр каталога")
    
    @task(1)
    def view_add_page(self):
        """Просмотр страницы добавления."""
        self.client.get("/add", name="Страница добавления")
    
    @task(1)
    def view_404(self):
        """Запрос несуществующей страницы (проверка обработки ошибок)."""
        self.client.get("/nonexistent-page", name="404 страница")


class HeavyUser(HttpUser):
    """
    Пользователь с тяжёлыми операциями (добавление данных).
    """
    
    wait_time = between(2, 8)
    
    @task(1)
    def add_language(self):
        """Добавление нового языка."""
        data = {
            "name": f"TestLang_{random.randint(1000, 9999)}",
            "year": str(random.randint(1990, 2024)),
            "creator": "Test Creator",
            "typing": random.choice(["Статическая", "Динамическая"]),
            "level": "Высокоуровневый",
            "difficulty": random.choice(["Лёгкий", "Средний", "Сложный"]),
            "categories": "Тестирование",
            "website": "https://test.com",
            "description": "Тестовый язык для нагрузочного тестирования",
            "history": "Создан автоматически",
            "code_example": 'print("test")',
        }
        self.client.post("/add/language", data=data, name="Добавление языка")
    
    @task(1)
    def add_library(self):
        """Добавление новой библиотеки."""
        data = {
            "name": f"TestLib_{random.randint(1000, 9999)}",
            "language": "Python",
            "year": str(random.randint(2000, 2024)),
            "category": "Тестирование",
            "website": "https://test.com",
            "description": "Тестовая библиотека для нагрузочного тестирования",
            "lore": "Создана автоматически",
        }
        self.client.post("/add/library", data=data, name="Добавление библиотеки")