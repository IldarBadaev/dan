from classes.Catalog import Catalog
from classes.Section import Section
import sys
sys.path.append('system/catalog/classes')


def section_list(SITE):
    print('FUNCTION -> system-> calalog -> section -> list')

    section_id = SITE.p[2]

    CATALOG = Catalog(SITE)
    SECTION = Section(SITE)
    section = SECTION.getSection(section_id)
    catalog = CATALOG.getItem(section['catalog_id'])

    row_out = '<tr><td>* * ТЕСТ * *<td><tr>'

    SITE.content += f'''<div class="bg_gray">
        <script>window.addEventListener("DOMContentLoaded", function(){{
        var contextmenu_item = [
            ["system/catalog/item/edit", "contextmenu_edit", "Редактировать элемент"],
            ["system/catalog/item/up", "contextmenu_up", "Вверх"],
            ["system/catalog/item/down", "contextmenu_down", "Вниз"],
            ["system/catalog/item/pub", "contextmenu_pub", "Опубликовать"],
            ["system/catalog/item/unpub", "contextmenu_unpub", "Скрыть"],
            ["system/catalog/item/delete", "contextmenu_delete", "Удалить элемент"]
        ];
        CONTEXTMENU.add("contextmenu_ico", contextmenu_item, "left");
        }})</script>
        <h1>Элементы раздела { section['name'] }</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>***</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/section/item_add/" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить элемент</div>
            </a>
            <a href="/system/section/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <table class="admin_table even_odd">
            <tr>
                <th style="width:50px;">Id</th>
                <th style="width:50px;">&nbsp;</th>
                <th>Наменование</th>
            </tr>
            { row_out }
        </table>
    </div>
    '''