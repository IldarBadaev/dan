class Section:
    def __init__(self, SITE):
        self.db = SITE.db
        self._tree_result = []

    def getItemsByCatalogId(self, catalog_id):
        sql = "SELECT id, parent_id, name, status FROM sections WHERE catalog_id = %s ORDER BY ordering"
        self.db.execute(sql, catalog_id)
        rows = self.db.fetchall()
        return rows if len(rows) > 0 else False
    
    def tree(self, catalog_id):
        rows = self.getItemsByCatalogId(catalog_id)
        self._recursion(rows)
        return self._tree_result
    
    def _recursion(self, rows, parent=0, level=-1):
        level += 1
        for row in rows:
            if int(row['parent_id']) == parent:
                self._tree_result.append({
                    'id': row['id'],
                    'name': row['name'],
                    'status': row['status'],
                    'level': level
                })
                self._recursion(rows, row['id'], level)
        return;