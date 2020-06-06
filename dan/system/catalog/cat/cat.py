from aiohttp import web
import re
import sys
sys.path.append('system/catalog/cat')
from edit import edit
from insert import insert
from cat_list import cat_list
from update import update
from ordering import ordering
from delete import delete
from settings_edit import settings_edit
from settings_update import settings_update
from sec_list import sec_list


def cat(SITE):
    print('PATH -> system/catalog/cat')

    # Вызов функций по ключу
    functions = {
        '': cat_list,
        'edit': edit,
        'add': edit,
        'insert': insert,
        'update': update,
        'up': ordering,
        'down': ordering,
        'delete': delete,
        'settings_edit': settings_edit,
        'settings_update': settings_update
    }

    print('SITE.p[2] = ', SITE.p[2])

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    if re.search('^\d+$', SITE.p[2]):
        return sec_list(SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
    
