from aiohttp import web
import re
import sys
sys.path.append('system/catalog/section')
from section_edit import section_edit
from section_insert import section_insert
from section_update import section_update
from section_ordering import section_ordering
from section_pub import section_pub
from section_delete import section_delete
from section_list import section_list


def section(SITE):
    print('PATH -> system/catalog/section')

    # Вызов функций по ключу
    functions = {
        'add': section_edit,
        'edit': section_edit,
        'insert': section_insert,
        'update': section_update,
        'up': section_ordering,
        'down': section_ordering,
        'pub': section_pub,
        'unpub': section_pub,
        'delete': section_delete,
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)
    
    if re.search('^\d+$', SITE.p[2]):
            return section_list(SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
