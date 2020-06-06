from classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def ordering(SITE):
    print('FUNCTION -> system-> calalog -> cat -> ordering')
    type = SITE.p[2]
    id = SITE.p[3]

    CATALOG = Catalog(SITE)
    catalog = CATALOG.ordering(type, id)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat'}
    return {'redirect': '/system/catalog/cat'}
