# data.py

languages = {
    "python": {
        "id": "python",
        "name": "Python",
        "year": 1991,
        "creator": "Гвидо ван Россум",
        "paradigm": "multi-paradigm",
        "typing": "Динамическая",
        "level": "Высокоуровневый",
        "categories": ["Веб", "Data Science", "Автоматизация", "ИИ"],
        "img": "/static/images/languages/python.webp",
        "website": "https://python.org",
        "difficulty": "Лёгкий",
        "popularity_rank": 1,
        "description": (
            "Python — высокоуровневый язык программирования общего назначения "
            "с акцентом на читаемость кода. Благодаря простому синтаксису "
            "и огромной экосистеме библиотек Python стал одним из самых "
            "популярных языков в мире."
        ),
        "history": (
            "Гвидо ван Россум начал разработку Python в конце 1980-х годов "
            "в Centrum Wiskunde & Informatica (Нидерланды). Первая версия "
            "вышла в 1991 году. Название вдохновлено комедийной группой "
            "Монти Пайтон, а не змеёй."
        ),
        "features": [
            {
                "name": "Простой синтаксис",
                "description": "Код на Python читается почти как английский текст. Отступы вместо фигурных скобок делают код визуально чистым.",
            },
            {
                "name": "Огромная экосистема",
                "description": "Более 400 000 пакетов на PyPI — для любой задачи от веб-разработки до машинного обучения.",
            },
            {
                "name": "Интерпретируемость",
                "description": "Python не требует компиляции — код выполняется построчно интерпретатором, что ускоряет разработку.",
            },
            {
                "name": "Кроссплатформенность",
                "description": "Работает на Windows, macOS, Linux и многих других платформах без изменения кода.",
            },
        ],
        "code_example": 'print("Hello, World!")',
    },

    "javascript": {
        "id": "javascript",
        "name": "JavaScript",
        "year": 1995,
        "creator": "Брендан Айк",
        "paradigm": "multi-paradigm",
        "typing": "Динамическая",
        "level": "Высокоуровневый",
        "categories": ["Веб", "Фронтенд", "Бэкенд", "Мобильные"],
        "img": "/static/images/languages/javascript.webp",
        "website": "https://developer.mozilla.org/ru/docs/Web/JavaScript",
        "difficulty": "Средний",
        "popularity_rank": 2,
        "description": (
            "JavaScript — язык программирования, который изначально создавался "
            "для добавления интерактивности на веб-страницы. Сегодня это один "
            "из самых универсальных языков, работающий как в браузере, "
            "так и на сервере."
        ),
        "history": (
            "Брендан Айк создал JavaScript за 10 дней в мае 1995 года, "
            "работая в компании Netscape. Изначально язык назывался Mocha, "
            "затем LiveScript, и наконец JavaScript — в рамках маркетинговой "
            "стратегии, связанной с популярностью Java."
        ),
        "features": [
            {
                "name": "Язык браузера",
                "description": "Единственный язык программирования, который нативно выполняется во всех веб-браузерах.",
            },
            {
                "name": "Асинхронность",
                "description": "Поддержка промисов и async/await позволяет эффективно работать с сетевыми запросами и вводом-выводом.",
            },
            {
                "name": "Универсальность",
                "description": "С помощью Node.js работает на сервере, с React Native — на мобильных, с Electron — на десктопе.",
            },
            {
                "name": "Событийная модель",
                "description": "Обработка событий — кликов, нажатий клавиш, загрузки данных — основа работы в браузере.",
            },
        ],
        "code_example": 'console.log("Hello, World!");',
    },

    "cpp": {
        "id": "cpp",
        "name": "C++",
        "year": 1985,
        "creator": "Бьёрн Страуструп",
        "paradigm": "multi-paradigm",
        "typing": "Статическая",
        "level": "Средне/Низкоуровневый",
        "categories": ["Системное ПО", "Игры", "Встраиваемые системы", "Высокая производительность"],
        "img": "/static/images/languages/cpp.webp",
        "website": "https://isocpp.org",
        "difficulty": "Сложный",
        "popularity_rank": 3,
        "description": (
            "C++ — мощный язык программирования, сочетающий низкоуровневое "
            "управление памятью с высокоуровневыми абстракциями. Используется "
            "там, где критична производительность: игры, операционные системы, "
            "браузеры, базы данных."
        ),
        "history": (
            "Бьёрн Страуструп начал работу над C++ в 1979 году в Bell Labs, "
            "создавая расширение языка C под названием «C with Classes». "
            "В 1985 году вышла первая коммерческая версия. С тех пор язык "
            "постоянно развивается, последние стандарты — C++20 и C++23."
        ),
        "features": [
            {
                "name": "Высокая производительность",
                "description": "Прямой доступ к памяти и отсутствие сборщика мусора дают максимальную скорость выполнения.",
            },
            {
                "name": "ООП и обобщённое программирование",
                "description": "Классы, наследование, полиморфизм, а также шаблоны для создания универсального кода.",
            },
            {
                "name": "Управление памятью",
                "description": "Программист сам контролирует выделение и освобождение памяти, что даёт гибкость и ответственность.",
            },
            {
                "name": "Совместимость с C",
                "description": "Почти любой код на C можно скомпилировать как C++, что даёт доступ к огромному наследию.",
            },
        ],
        "code_example": '#include <iostream>\nint main() {\n    std::cout << "Hello, World!";\n    return 0;\n}',
    },

    "java": {
        "id": "java",
        "name": "Java",
        "year": 1995,
        "creator": "Джеймс Гослинг",
        "paradigm": "object-oriented",
        "typing": "Статическая",
        "level": "Высокоуровневый",
        "categories": ["Корпоративное ПО", "Android", "Веб", "Финтех"],
        "img": "/static/images/languages/java.webp",
        "website": "https://www.java.com",
        "difficulty": "Средний",
        "popularity_rank": 4,
        "description": (
            "Java — объектно-ориентированный язык с принципом «написал один раз — "
            "запускай везде». Код компилируется в байт-код, который выполняется "
            "на виртуальной машине JVM, обеспечивая кроссплатформенность."
        ),
        "history": (
            "Разработка началась в 1991 году в Sun Microsystems под руководством "
            "Джеймса Гослинга. Проект назывался «Green» и предназначался для "
            "встраиваемых устройств. Публичный релиз состоялся в 1995 году. "
            "В 2010 году Oracle приобрела Sun Microsystems вместе с Java."
        ),
        "features": [
            {
                "name": "Write Once, Run Anywhere",
                "description": "Благодаря JVM один и тот же скомпилированный код работает на любой платформе.",
            },
            {
                "name": "Сборщик мусора",
                "description": "Автоматическое управление памятью избавляет от ручного выделения и освобождения ресурсов.",
            },
            {
                "name": "Строгая типизация",
                "description": "Все переменные имеют фиксированный тип, ошибки обнаруживаются на этапе компиляции.",
            },
            {
                "name": "Многопоточность",
                "description": "Встроенная поддержка потоков позволяет эффективно использовать многоядерные процессоры.",
            },
        ],
        "code_example": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
    },

    "rust": {
        "id": "rust",
        "name": "Rust",
        "year": 2015,
        "creator": "Грейдон Хор (Mozilla)",
        "paradigm": "multi-paradigm",
        "typing": "Статическая",
        "level": "Системный",
        "categories": ["Системное ПО", "WebAssembly", "CLI-утилиты", "Безопасность"],
        "img": "/static/images/languages/rust.webp",
        "website": "https://www.rust-lang.org",
        "difficulty": "Сложный",
        "popularity_rank": 5,
        "description": (
            "Rust — системный язык программирования, ориентированный на "
            "безопасность, скорость и параллелизм. Уникальная система "
            "владения (ownership) предотвращает ошибки работы с памятью "
            "на этапе компиляции без сборщика мусора."
        ),
        "history": (
            "Грейдон Хор начал работу над Rust как личный проект в 2006 году. "
            "В 2009 году Mozilla начала спонсировать разработку. Первый стабильный "
            "релиз Rust 1.0 вышел в мае 2015 года. С тех пор Rust неизменно "
            "занимает первое место в опросе Stack Overflow как самый любимый язык."
        ),
        "features": [
            {
                "name": "Система владения (Ownership)",
                "description": "Уникальная модель управления памятью: каждое значение имеет одного владельца, что исключает утечки и гонки данных.",
            },
            {
                "name": "Безопасность без сборщика мусора",
                "description": "Компилятор проверяет корректность работы с памятью на этапе сборки — ошибки невозможны в рантайме.",
            },
            {
                "name": "Нулевая стоимость абстракций",
                "description": "Высокоуровневые конструкции компилируются в такой же эффективный код, как ручная низкоуровневая реализация.",
            },
            {
                "name": "Cargo",
                "description": "Встроенный менеджер пакетов и система сборки — один инструмент для управления зависимостями и компиляции.",
            },
        ],
        "code_example": 'fn main() {\n    println!("Hello, World!");\n}',
    },
}


libraries = {
    "django": {
        "id": "django",
        "name": "Django",
        "language": "Python",
        "language_id": "python",
        "year": 2005,
        "category": "Веб-фреймворк",
        "img": "/static/images/libraries/django.webp",
        "website": "https://www.djangoproject.com",
        "description": (
            "Django — высокоуровневый веб-фреймворк для Python, который "
            "поощряет быструю разработку и чистый, прагматичный дизайн. "
            "Включает ORM, систему аутентификации, админ-панель и многое другое."
        ),
        "lore": "Назван в честь джазового гитариста Джанго Рейнхардта.",
        "stats": {
            "stars_github": "75k+",
            "лицензия": "BSD",
            "последняя_версия": "5.x",
        },
        "active": {
            "name": "Batteries included",
            "description": "Django включает всё необходимое из коробки: ORM, маршрутизацию, шаблоны, формы, аутентификацию.",
            "cooldown": 0,
            "mana_cost": 0,
        },
    },
    "react": {
        "id": "react",
        "name": "React",
        "language": "JavaScript",
        "language_id": "javascript",
        "year": 2013,
        "category": "UI-библиотека",
        "img": "/static/images/libraries/react.webp",
        "website": "https://react.dev",
        "description": (
            "React — библиотека для создания пользовательских интерфейсов, "
            "разработанная Facebook. Использует компонентный подход и "
            "виртуальный DOM для эффективного обновления страниц."
        ),
        "lore": "Создана Джорданом Уолке в Facebook для решения проблем с производительностью интерфейса.",
        "stats": {
            "stars_github": "220k+",
            "лицензия": "MIT",
            "последняя_версия": "18.x",
        },
        "active": {
            "name": "Virtual DOM",
            "description": "React создаёт виртуальную копию DOM и обновляет только изменившиеся элементы, что повышает скорость.",
            "cooldown": 0,
            "mana_cost": 0,
        },
    },
    "spring": {
        "id": "spring",
        "name": "Spring",
        "language": "Java",
        "language_id": "java",
        "year": 2003,
        "category": "Веб-фреймворк",
        "img": "/static/images/libraries/spring.webp",
        "website": "https://spring.io",
        "description": (
            "Spring — мощный фреймворк для создания корпоративных Java-приложений. "
            "Spring Boot упрощает конфигурацию и позволяет запустить проект за минуты."
        ),
        "lore": "Создан Родом Джонсоном как альтернатива сложным Enterprise JavaBeans.",
        "stats": {
            "stars_github": "55k+",
            "лицензия": "Apache 2.0",
            "последняя_версия": "6.x",
        },
        "active": {
            "name": "Dependency Injection",
            "description": "Автоматическое внедрение зависимостей делает код слабосвязанным и легко тестируемым.",
            "cooldown": 0,
            "mana_cost": 0,
        },
    },
    "tokio": {
        "id": "tokio",
        "name": "Tokio",
        "language": "Rust",
        "language_id": "rust",
        "year": 2016,
        "category": "Асинхронный рантайм",
        "img": "/static/images/libraries/tokio.webp",
        "website": "https://tokio.rs",
        "description": (
            "Tokio — асинхронный рантайм для Rust, обеспечивающий "
            "написание надёжных сетевых приложений. Используется "
            "для серверов, баз данных и CLI-инструментов."
        ),
        "lore": "Название вдохновлено городом Токио — символом скорости и технологий.",
        "stats": {
            "stars_github": "24k+",
            "лицензия": "MIT",
            "последняя_версия": "1.x",
        },
        "active": {
            "name": "Async Runtime",
            "description": "Предоставляет планировщик задач, таймеры, ввод-вывод — всё для асинхронного программирования.",
            "cooldown": 0,
            "mana_cost": 0,
        },
    },
    "qt": {
        "id": "qt",
        "name": "Qt",
        "language": "C++",
        "language_id": "cpp",
        "year": 1995,
        "category": "GUI-фреймворк",
        "img": "/static/images/libraries/qt.webp",
        "website": "https://www.qt.io",
        "description": (
            "Qt — кроссплатформенный фреймворк для создания графических "
            "приложений на C++. Используется в KDE, Autodesk Maya, "
            "VLC и многих других программах."
        ),
        "lore": "Разработан в Норвегии компанией Trolltech. Буква Q выбрана, потому что красиво выглядела в шрифте Emacs.",
        "stats": {
            "stars_github": "Open Source edition",
            "лицензия": "LGPL / Commercial",
            "последняя_версия": "6.x",
        },
        "active": {
            "name": "Signals & Slots",
            "description": "Механизм связи между объектами: один объект посылает сигнал, другой — реагирует через слот.",
            "cooldown": 0,
            "mana_cost": 0,
        },
    },
}


# =============================================
# Вспомогательные функции
# =============================================

def get_all_languages():
    """Возвращает список всех языков"""
    return list(languages.values())


def get_language(lang_id: str):
    """Возвращает язык по ID или None"""
    return languages.get(lang_id)


def get_all_libraries():
    """Возвращает список всех библиотек"""
    return list(libraries.values())


def get_library(lib_id: str):
    """Возвращает библиотеку по ID или None"""
    return libraries.get(lib_id)


def get_all_content():
    """
    Возвращает единый список из языков и библиотек.
    К каждому элементу добавляется поле 'content_type',
    чтобы в шаблоне можно было отличить язык от библиотеки.
    """
    content = []

    for lang in languages.values():
        item = dict(lang)                # копируем словарь
        item["content_type"] = "language" # помечаем тип
        content.append(item)

    for lib in libraries.values():
        item = dict(lib)
        item["content_type"] = "library"
        content.append(item)

    return content


def add_language(lang_data: dict):
    """
    Добавляет новый язык в словарь.
    Возвращает кортеж (lang_id, is_duplicate).
    """
    lang_id = lang_data["name"].lower().replace(" ", "_").replace("+", "plus").replace("#", "sharp")

    # Проверка на дубликат
    if lang_id in languages:
        return (lang_id, True)  # Дубликат найден

    languages[lang_id] = {
        "id": lang_id,
        "name": lang_data["name"],
        "year": int(lang_data.get("year", 2024)),
        "creator": lang_data.get("creator", "Неизвестен"),
        "paradigm": lang_data.get("paradigm", "multi-paradigm"),
        "typing": lang_data.get("typing", "Динамическая"),
        "level": lang_data.get("level", "Высокоуровневый"),
        "categories": [
            cat.strip()
            for cat in lang_data.get("categories", "Общее").split(",")
        ],
        "img": "",
        "website": lang_data.get("website", ""),
        "difficulty": lang_data.get("difficulty", "Средний"),
        "popularity_rank": len(languages) + 1,
        "description": lang_data.get("description", "Описание не указано."),
        "history": lang_data.get("history", "История не указана."),
        "features": [],
        "code_example": lang_data.get("code_example", "// Hello, World!"),
    }

    return (lang_id, False)


def add_library(lib_data: dict):
    """
    Добавляет новую библиотеку в словарь.
    Возвращает кортеж (lib_id, is_duplicate).
    """
    lib_id = lib_data["name"].lower().replace(" ", "_").replace(".", "")

    # Проверка на дубликат
    if lib_id in libraries:
        return (lib_id, True)

    # Определяем language_id по названию языка
    language_name = lib_data.get("language", "")
    language_id = ""
    for lang in languages.values():
        if lang["name"].lower() == language_name.lower():
            language_id = lang["id"]
            break

    libraries[lib_id] = {
        "id": lib_id,
        "name": lib_data["name"],
        "language": lib_data.get("language", "Не указан"),
        "language_id": language_id,
        "year": int(lib_data.get("year", 2024)),
        "category": lib_data.get("category", "Библиотека"),
        "img": "",
        "website": lib_data.get("website", ""),
        "description": lib_data.get("description", "Описание не указано."),
        "lore": lib_data.get("lore", ""),
        "stats": {},
        "active": None,
    }

    return (lib_id, False)


def search_all(query: str):
    """Ищет языки и библиотеки по имени."""
    query_lower = query.lower().strip()
    
    # Специальная обработка для C++
    query_variations = [query_lower]
    if "c++" in query_lower or "c  " in query_lower:
        query_variations.append("c++")
        query_variations.append("cpp")

    found_languages = []
    for lang in languages.values():
        name_lower = lang["name"].lower()
        id_lower = lang["id"].lower()
        
        # Проверяем все вариации запроса
        for variant in query_variations:
            if variant in name_lower or variant in id_lower:
                if lang not in found_languages:
                    found_languages.append(lang)
                break

    found_libraries = []
    for lib in libraries.values():
        name_lower = lib["name"].lower()
        lang_lower = lib["language"].lower()
        id_lower = lib["id"].lower()
        
        for variant in query_variations:
            if variant in name_lower or variant in lang_lower or variant in id_lower:
                if lib not in found_libraries:
                    found_libraries.append(lib)
                break

    return {
        "languages": found_languages,
        "libraries": found_libraries,
        "total": len(found_languages) + len(found_libraries),
    }