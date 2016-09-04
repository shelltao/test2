# coding:utf-8


from settings import DB_PATH


class StoreError(Exception):
    pass


class DB(object):
    def __init__(self, path=DB_PATH):
        self.index_lines = {}
        self.path = path

        with open(self.path) as f:
            for line in f:
                _id = int(line.split(' ')[0])
                self.index_lines[_id] = line.strip()

        self.max_id = max(self.index_lines.keys() or [0])

    def insert(self, columns):
        self.max_id += 1
        columns.insert(0, str(self.max_id))
        line = ' '.join(columns)

        self.index_lines[self.max_id] = line

        self._store()

    def update(self, _id, columns):
        columns.insert(0, str(_id))
        line = ' '.join(columns)

        self.index_lines[_id] = line

        self._store()

    def query_by_id(self, _id):
        assert _id in self.index_lines, '指定id不存在'

        line = self.index_lines[_id]
        return line.split(' ')

    def delete_by_id(self, _id):
        assert _id in self.index_lines, '指定id不存在'

        line = self.index_lines.pop(_id)

        self._store()
        return line.split(' ')

    def _store(self):
        try:
            with open(self.path, 'w') as f:
                f.writelines(self.index_lines.values())
        except Exception as e:
            # 检测文件权限
            print '权限为只读，请修改权限'
            raise StoreError(e)
