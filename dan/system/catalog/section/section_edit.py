from classes.Catalog import Catalog
import sys
sys.path.append('system/catalog/classes')


def section_edit(SITE):
    print('PATH -> system/catalog/section/edit')

    if SITE.p[2] == 'edit':
        # SECTION = Section(SITE)
        # section = SECTION.getItem(SITE.p[3])
        title = 'Редактировать раздел'
        action = 'update/' + SITE.p[3]
    else:
        title = 'Добавить  раздел'
        action = 'insert'
        # ordering = SECTION.getMaxOrdering() + 1
        ordering = 1
        section = {'name': '', 'url': '', 'ordering': ordering}

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog/cat">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
			<a href="/system/catalog/cat">Добавить раздел</a>
            <span>''' + title + '''</span>
        </div>
		<form method="post" action="/system/catalog/system/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="name" placeholder="Раздел 1" required value="''' + section['name'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Порядок следования</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="ordering" type="number" value="''' + str(section['ordering']) + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
		</form>
    </div>
    '''
