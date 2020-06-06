from classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def settings_update(SITE):
    print('FUNCTION -> system-> calalog -> cat -> settings_update')
    
    CATALOG = Catalog(SITE)
    catalog = CATALOG.settingsUpdate(SITE.p[3], SITE.post['settings'])  # Удаляем текущий элемент

    return {'redirect': '/system/catalog/cat'}