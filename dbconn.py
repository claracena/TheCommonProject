import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db = 'common.sqlite'):
        self.db = db
        self.conn = None
        self.cursor = None
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
        except Error as e:
            print(e)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

    def select_all_participants(self):
        self.cursor.execute('SELECT * FROM participants')
        rows = self.cursor.fetchall()
        return rows

    def select_a_participant(self, participant_id):
        sql = 'SELECT * FROM participants WHERE id = ?'
        arg = (participant_id, )
        self.cursor.execute(sql, arg)
        rows = self.cursor.fetchall()
        return rows

    def select_all_categories(self):
        sql = 'SELECT * FROM categories WHERE enabled = ?'
        arg = (1, )
        self.cursor.execute(sql, arg)
        rows = self.cursor.fetchall()
        return rows

    def select_all_modules_from_cateory(self, cat_id):
        sql = 'SELECT * FROM modules WHERE category = ? AND enabled = ?'
        arg = (cat_id, 1)
        self.cursor.execute(sql, arg)
        rows = self.cursor.fetchall()
        return rows

    def select_module(self, module):
        sql = '''SELECT
                    modules.id,
                    modules.name,
                    modules.description,
                    participants.fname,
                    participants.lname,
                    participants.display_name,
                    categories.category_name,
                    modules.filename
                FROM modules
                JOIN participants ON modules.author = participants.id
                JOIN categories ON modules.category = categories.id
                WHERE modules.id = ?
                AND modules.enabled = ?'''
        arg = (module, 1)
        self.cursor.execute(sql, arg)
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            result = {'module_id': rows[0][0],
                        'module_name': rows[0][1],
                        'module_desc': rows[0][2],
                        'module_auth_name': rows[0][3] + ' ' + rows[0][4],
                        'module_auth_display_name': rows[0][5],
                        'module_category': rows[0][6],
                        'module_filename': rows[0][7]}
        else:
            result = {}
        return result