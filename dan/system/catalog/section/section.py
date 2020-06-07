from aiohttp import web
import sys
sys.path.append('system/catalog/section')
from section_edit import section_edit
#from insert import insert
#from cat_list import cat_list
#from update import update
#from ordering import ordering
#from delete import delete
#from settings_edit import settings_edit
#from settings_update import settings_update
#from sec_list import sec_list


def section(SITE):
    print('PATH -> system/catalog/section')

    # Вызов функций по ключу
    functions = {
        'add': section_edit,
        # 'edit': edit,
        # 'insert': insert,
        # 'update': update,
        # 'up': ordering,
        # 'down': ordering,
        # 'delete': delete,
        # 'settings_edit': settings_edit,
        # 'settings_update': settings_update
    }

    if (SITE.p[2] in functions):
        return functions[SITE.p[2]](SITE)

    # Если функция не существует и это не номер раздела - 404
    raise web.HTTPNotFound()
