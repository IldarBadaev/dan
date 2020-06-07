class Section:
    def __init__(self, SITE):
        self.db = SITE.db
        self._tree_result = []

    def getSection(self, id):
        sql = "SELECT `id`, `catalog_id`, `parent_id`, `name`, `text`, `data`, `status`, `ordering` FROM sections WHERE id = %s"
        self.db.execute(sql, id)
        return self.db.fetchone()

    def getSectionsByCatalogId(self, catalog_id):
        sql = "SELECT `id`, `parent_id`, `name`, `text`, `data`, `status` FROM sections WHERE catalog_id = %s ORDER BY ordering"
        self.db.execute(sql, catalog_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False

    def insert(self, data):
        sql = "INSERT INTO sections SET `catalog_id` = %s, `parent_id` = %s, `name` = %s, `image` = '', `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s"
        return self.db.execute(sql, (
            data['catalog_id'],
            data['parent_id'],
            data['name'],
            data['text'],
            data['data'],
            data['status'],
            data['ordering']
        ))

    def update(self, data):
        sql = "UPDATE sections SET `parent_id` = %s, `name` = %s, `image` = '', `text` = %s, `data` = %s, `date` = NOW(), `status` = %s, `ordering` = %s WHERE id = %s"
        return self.db.execute(sql, (
            data['parent_id'],
            data['name'],
            data['text'],
            data['data'],
            data['status'],
            data['ordering'],
            data['id']
        ))

    def tree(self, catalog_id):
        rows = self.getSectionsByCatalogId(catalog_id)
        self._recursion(rows)
        return self._tree_result

    def _recursion(self, rows, parent=0, level=-1):
        level += 1
        for row in rows:
            if int(row['parent_id']) == parent:
                self._tree_result.append({
                    'id': row['id'],
                    'parent_id': row['parent_id'],
                    'name': row['name'],
                    'status': row['status'],
                    'level': level
                })
                self._recursion(rows, row['id'], level)
        return
