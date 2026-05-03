# main.py

import traceback
from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import (
    get_all_languages, get_language,
    get_all_libraries, get_library,
    get_all_content,
    add_language, add_library,
    search_all,
)


app = FastAPI(title="Programming Languages Wiki")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Перехватчик ошибок
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    error_text = traceback.format_exc()
    print(error_text)
    return PlainTextResponse(
        content=f"Ошибка:\n\n{error_text}",
        status_code=500,
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    all_languages = get_all_languages()
    all_libraries = get_all_libraries()
    all_content = get_all_content()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Programming Wiki",
            "languages": all_languages[:3],
            "libraries": all_libraries[:3],
            "all_content": all_content,
        },
    )


@app.get("/languages", response_class=HTMLResponse)
async def languages_list(
    request: Request,
    typing_filter: str = Query(default=None, alias="typing"),
):
    all_languages = get_all_languages()

    if typing_filter and typing_filter in ("Статическая", "Динамическая"):
        all_languages = [
            lang for lang in all_languages
            if lang["typing"] == typing_filter
        ]

    return templates.TemplateResponse(
        "languages.html",
        {
            "request": request,
            "title": "Языки программирования",
            "languages": all_languages,
            "current_typing": typing_filter,
        },
    )


@app.get("/language/{lang_id}", response_class=HTMLResponse)
async def language_detail(request: Request, lang_id: str):
    lang = get_language(lang_id)

    if not lang:
        return RedirectResponse(url="/languages")

    creator_short = lang["creator"].split(" ")[-1]

    return templates.TemplateResponse(
        "language.html",
        {
            "request": request,
            "title": lang["name"],
            "lang": lang,
            "creator_short": creator_short,
        },
    )


@app.get("/libraries", response_class=HTMLResponse)
async def libraries_list(request: Request):
    all_libraries = get_all_libraries()
    return templates.TemplateResponse(
        "libraries.html",
        {
            "request": request,
            "title": "Библиотеки и фреймворки",
            "libraries": all_libraries,
        },
    )

@app.get("/catalog", response_class=HTMLResponse)
async def catalog(request: Request):
    """Страница со всем содержимым — языки и библиотеки вместе."""
    all_content = get_all_content()
    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "title": "Весь каталог",
            "all_content": all_content,
        },
    )


@app.get("/library/{lib_id}", response_class=HTMLResponse)
async def library_detail(request: Request, lib_id: str):
    lib = get_library(lib_id)

    if not lib:
        return RedirectResponse(url="/libraries")

    return templates.TemplateResponse(
        "library.html",
        {
            "request": request,
            "title": lib["name"],
            "lib": lib,
        },
    )


# --- Страница добавления контента ---

@app.get("/add", response_class=HTMLResponse)
async def add_page(
    request: Request,
    success: str = Query(default=None),
):
    """Показывает форму добавления языка или библиотеки."""
    return templates.TemplateResponse(
        "add.html",
        {
            "request": request,
            "title": "Добавить запись",
            "success": success,
        },
    )


@app.post("/add/language")
async def add_language_handler(
    request: Request,
    name: str = Form(...),
    year: str = Form("2024"),
    creator: str = Form("Неизвестен"),
    typing: str = Form("Динамическая"),
    level: str = Form("Высокоуровневый"),
    difficulty: str = Form("Средний"),
    categories: str = Form("Общее"),
    website: str = Form(""),
    description: str = Form(""),
    history: str = Form(""),
    code_example: str = Form(""),
):
    """Обрабатывает форму добавления языка."""
    lang_data = {
        "name": name,
        "year": year,
        "creator": creator,
        "typing": typing,
        "level": level,
        "difficulty": difficulty,
        "categories": categories,
        "website": website,
        "description": description,
        "history": history,
        "code_example": code_example,
    }

    lang_id = add_language(lang_data)
    return RedirectResponse(
        url=f"/add?success=language:{lang_id}",
        status_code=303,
    )


@app.post("/add/library")
async def add_library_handler(
    request: Request,
    name: str = Form(...),
    language: str = Form(""),
    year: str = Form("2024"),
    category: str = Form("Библиотека"),
    website: str = Form(""),
    description: str = Form(""),
    lore: str = Form(""),
):
    """Обрабатывает форму добавления библиотеки."""
    lib_data = {
        "name": name,
        "language": language,
        "year": year,
        "category": category,
        "website": website,
        "description": description,
        "lore": lore,
    }

    lib_id = add_library(lib_data)
    return RedirectResponse(
        url=f"/add?success=library:{lib_id}",
        status_code=303,
    )


@app.get("/search", response_class=HTMLResponse)
async def search(
    request: Request,
    q: str = Query(default="", description="Поисковый запрос"),
):
    results = search_all(q) if q else {"languages": [], "libraries": [], "total": 0}

    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "title": f"Поиск: {q}",
            "query": q,
            "results": results,
        },
    )