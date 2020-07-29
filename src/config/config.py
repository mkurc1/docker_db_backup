from .db_connector import DbConnector
from tabulate import tabulate


class Config:
    def __init__(self):
        self.db_connector = DbConnector('config', 'config')

    def run(self):
        self.menu()

    def list(self):
        print(tabulate(self.db_connector.list(), headers=[
            "Row ID",
            "Container name or ID",
            "Root password into DB",
            "Database name"
        ]))

    def add(self):
        row_id = int(input('Row ID: > '))
        container = input('Container name or ID: > ')
        root_pass = input('Root password into DB: > ')
        db_name = input('Database name: > ')

        self.db_connector.add(row_id, container, root_pass, db_name)

    def edit(self):
        row_id = int(input('Row ID: > '))
        container = input('Container name or ID: > ')
        root_pass = input('Root password into DB: > ')
        db_name = input('Database name: > ')

        self.db_connector.edit(row_id, container, root_pass, db_name)

    def remove(self):
        row_id = int(input('Row ID: > '))
        self.db_connector.delete(row_id)

    def menu(self):
        while True:
            print()
            self.list()
            print()
            print('Press `1` to add new config')
            print('Press `2` to edit config')
            print('Press `3` to remove config')
            print('Press `q` to quit')
            select = input('Select your option and press `Enter` > ').lower().strip()
            print()

            if select == 'q':
                break
            elif select == '1':
                self.add()
            elif select == '2':
                self.edit()
            elif select == '3':
                self.remove()
            else:
                print('Invalid choice!')
