import traceback
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import (
    get_all_languages, get_language,
    get_all_libraries, get_library,
    search_all,
)


app = FastAPI(title="Programming Languages Wiki")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Перехватчик ошибок. НЕ ТРОГАТЬ! 
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    error_text = traceback.format_exc()
    print(error_text)  # вывод в терминал 
    return PlainTextResponse(
        content=f"Ошибка:\n\n{error_text}",
        status_code=500,
    )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    all_languages = get_all_languages()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Programming Wiki",
            "languages": all_languages[:3],
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