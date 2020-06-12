from classes.Section import Section
import sys
sys.path.append('system/catalog/classes')


def section_ordering(SITE):
    print('FUNCTION -> system-> calalog -> section -> ordering')
    type = SITE.p[2]
    id = SITE.p[3]

    SECTION = Section(SITE)
    cat_id = SECTION.ordering(type, id)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + str(cat_id)}
    return {'redirect': '/system/catalog/cat/' + str(cat_id)}
