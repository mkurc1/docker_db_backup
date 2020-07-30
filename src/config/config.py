from .db_connector import DbConnector
from tabulate import tabulate
import click


class Config:
    def __init__(self):
        self.db_connector = DbConnector('config', 'config')

    def run(self):
        self.menu()

    def list(self):
        click.echo(tabulate(self.db_connector.list(), headers=[
            "Row ID",
            "Container name or ID",
            "Root password into DB",
            "Database name"
        ]))

    def add(self):
        row_id = click.prompt('Row ID', type=int)
        container = click.prompt('Container name or ID')
        root_pass = click.prompt('Root password into DB')
        db_name = click.prompt('Database name')

        self.db_connector.add(row_id, container, root_pass, db_name)

    def edit(self):
        row_id = click.prompt('Row ID', type=int)
        container = click.prompt('Container name or ID')
        root_pass = click.prompt('Root password into DB')
        db_name = click.prompt('Database name')

        self.db_connector.edit(row_id, container, root_pass, db_name)

    def remove(self):
        row_id = click.prompt('Row ID', type=int)
        self.db_connector.delete(row_id)

    def menu(self):
        while True:
            click.echo()
            self.list()
            click.echo()
            click.echo('Press `1` to add new config')
            click.echo('Press `2` to edit config')
            click.echo('Press `3` to remove config')
            click.echo('Press `q` to quit')
            select = click.prompt('Select your option and press `Enter').lower().strip()
            click.echo()

            if select == 'q':
                break
            elif select == '1':
                self.add()
            elif select == '2':
                self.edit()
            elif select == '3':
                self.remove()
            else:
                click.echo('Invalid choice!')
