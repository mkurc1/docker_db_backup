import sqlite3
import os


class DbConnector:
    def __init__(self, file_name, table_name):
        self.table_name = table_name
        self.db_path = os.path.join(os.path.dirname(__file__) + '/../../data/', f'{file_name}.sqlite3')
        self.create_table_if_not_exist()

    def get_conn(self):
        return sqlite3.connect(self.db_path)

    def execute(self, query, params=()):
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.commit()
        conn.close()

        return result

    def create_table_if_not_exist(self):
        result = self.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = ?",
                              (self.table_name,))
        if result[0][0] != 1:
            self.execute(f"""CREATE TABLE {self.table_name} (
                    id INTEGER PRIMARY KEY, 
                    container TEXT NOT NULL, 
                    root_pass TEXT NOT NULL, 
                    db_name TEXT NOT NULL
                )""")

    def add(self, row_id, container, root_pass, db_name):
        try:
            self.execute(f"INSERT INTO {self.table_name}(id, container, root_pass, db_name) values (?, ?, ?, ?)",
                         (row_id, container, root_pass, db_name))
        except sqlite3.IntegrityError:
            print(f'Row with that ID: `{row_id}` already exist.')

    def edit(self, row_id, container, root_pass, db_name):
        self.execute(f"UPDATE {self.table_name} SET container = ?, root_pass = ?, db_name = ? WHERE id = ?",
                     (container, root_pass, db_name, row_id))

    def get(self, row_id):
        return self.execute(f"SELECT * FROM {self.table_name} WHERE id = ?", (row_id,))

    def delete(self, row_id):
        self.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (row_id,))

    def list(self):
        return self.execute(f"SELECT * FROM {self.table_name}")
