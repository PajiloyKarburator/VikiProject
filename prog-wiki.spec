# prog-wiki.spec
# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_all, collect_submodules

block_cipher = None

# Собираем все подмодули критичных пакетов
fastapi_hidden = collect_submodules('fastapi')
starlette_hidden = collect_submodules('starlette')
uvicorn_hidden = collect_submodules('uvicorn')
jinja2_hidden = collect_submodules('jinja2')
pydantic_hidden = collect_submodules('pydantic')
anyio_hidden = collect_submodules('anyio')

# Собираем данные (templates, статика и т.д.)
fastapi_datas, fastapi_binaries, fastapi_hidden2 = collect_all('fastapi')
starlette_datas, starlette_binaries, starlette_hidden2 = collect_all('starlette')
uvicorn_datas, uvicorn_binaries, uvicorn_hidden2 = collect_all('uvicorn')

all_hidden = (
    fastapi_hidden + starlette_hidden + uvicorn_hidden + 
    jinja2_hidden + pydantic_hidden + anyio_hidden +
    fastapi_hidden2 + starlette_hidden2 + uvicorn_hidden2
)

all_datas = fastapi_datas + starlette_datas + uvicorn_datas
all_binaries = fastapi_binaries + starlette_binaries + uvicorn_binaries

a = Analysis(
    ['start_debug.py'],
    pathex=[],
    binaries=all_binaries,
    datas=[
        ('static', 'static'),
        ('templates', 'templates'),
        ('data.py', '.'),
        ('main.py', '.'),
    ] + all_datas,
    hiddenimports=all_hidden + [
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.http.h11_impl',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.protocols.websockets.wsproto_impl',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'click',
        'h11',
        'httptools',
        'websockets',
        'watchfiles',
        'multipart',
        'email.mime',
        'email.mime.multipart',
        'email.mime.text',
        'typing_extensions',
        'pydantic_core',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ProgWiki',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ProgWiki',
)