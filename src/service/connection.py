from service.db_connector import DbConnector
from tabulate import tabulate
import click


class Connection:
    def __init__(self):
        self.__db_connector = DbConnector('config', 'config')

    def list(self):
        click.echo(tabulate(self.__db_connector.list(), headers=[
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

        self.__db_connector.add(row_id, container, root_pass, db_name)

    def edit(self):
        row_id = click.prompt('Row ID', type=int)
        container = click.prompt('Container name or ID')
        root_pass = click.prompt('Root password into DB')
        db_name = click.prompt('Database name')

        self.__db_connector.edit(row_id, container, root_pass, db_name)

    def remove(self):
        row_id = click.prompt('Row ID', type=int)
        self.__db_connector.delete(row_id)
