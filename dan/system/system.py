from aiohttp import web
import sys
sys.path.append('system')
sys.path.append('system/catalog')
from catalog import catalog
from mainpage import mainpage

def router(SITE):
    print('SYSTEM - router')
    auth = 0

    if (auth != 1):
        # Если нет авторизации
        if (SITE.request.method == 'POST' and SITE == 'login'):
            print ('Проверка логина / пароля')
        else:
            print ('Редирект на страницу SYSTEM')

        # Вызов функций по ключу
        functions = {
            '': mainpage,
            'catalog': catalog
            # 'users': users,
            # 'help': help
        }

        if (SITE.p[0] not in functions):
            # Если функция не существует - 404
            raise web.HTTPNotFound()

        # Вызов функции
        return functions[SITE.p[0]](SITE)
