from classes.Section import Section
import sys
sys.path.append('system/catalog/classes')


def section_pub(SITE):
    print('FUNCTION -> system-> calalog -> section -> pub/unpub')
    type = SITE.p[2]
    id = SITE.p[3]

    SECTION = Section(SITE)
    cat_id = SECTION.pub(type, id)

    if 'cancel' in SITE.post:
        return {'redirect': '/system/catalog/cat/' + str(cat_id)}
    return {'redirect': '/system/catalog/cat/' + str(cat_id)}