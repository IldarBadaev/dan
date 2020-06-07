from aiohttp import web
import re
import sys
sys.path.append('system/catalog/cat')
from cat_edit import cat_edit
from cat_insert import cat_insert
from cat_list import cat_list
from cat_update import cat_update
from cat_ordering import cat_ordering
from cat_delete import cat_delete
from cat_settings_edit import cat_settings_edit
from cat_settings_update import cat_settings_update
from cat_sec_list import cat_sec_list


def cat(SITE):
    print('PATH -> system/catalog/cat')

    # Вызов функций по ключу
    functions = {
        '': cat_list,
        'edit': cat_edit,
        'add': cat_edit,
        'insert': cat_insert,
        'update': cat_update,
        'up': cat_ordering,
        'down': cat_ordering,
        'delete': cat_delete,
        'settings_edit': cat_settings_edit,
        'settings_update': cat_settings_update,
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    if re.search('^\d+$', SITE.p[2]):
        return cat_sec_list(SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
    
