from classes.Section import Section
import sys
sys.path.append('system/catalog/classes')


def section_delete(SITE):
    print('FUNCTION -> system-> calalog -> section -> delete')

    id = SITE.post['id']

    SECTION = Section(SITE)

    if 'agree' in SITE.post and SITE.post['agree'] == 'yes':
        cat_id = SECTION.delete(id)
    else:
        cat_id = SECTION.getSection(id)['catalog_id']

    return {'redirect': '/system/catalog/cat/' + str(cat_id)}