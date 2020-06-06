from aiohttp import web
import sys
sys.path.append('system/catalog/cat')
from cat import cat


def catalog(SITE):
    print('PATH -> system/catalog')

    # Вызов функций по ключу
    functions = {
        '': cat,  # Управление каталогами
        'cat': cat
        # 'section': section,
        # 'item': item,
        # 'settings': settings,
        # 'char': char
    }

    print('SITE.p[1] = ', SITE.p[1])

    if (SITE.p[1] not in functions):
        # Если функция не существует - 404
        raise web.HTTPNotFound()

    # Вызов функции
    return functions[SITE.p[1]](SITE)
