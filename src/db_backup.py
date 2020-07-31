import click
import os

from service.connection import Connection
from service.backup import Backup

from dotenv import load_dotenv

connection = Connection()
load_dotenv()


@click.group()
def main():
    """
    DB Backup\n
    App allow to backup mysql database located in docker containers and send it into Object Storage.
    """
    pass


@main.command('backup')
def backup_cmd():
    """Process backup"""
    dump_dir = os.path.join(os.path.dirname(__file__) + '/../data/')
    backup = Backup(dump_dir)
    backup.process()


@main.command('list')
def list_cmd():
    """List of all database connections"""
    connection.list()


@main.command('add')
def add_cmd():
    """Add new connection"""
    connection.add()


@main.command('edit')
def edit_cmd():
    """Edit exist connection"""
    connection.edit()


@main.command('remove')
def edit_cmd():
    """Remove exist connection"""
    connection.remove()


if __name__ == '__main__':
    main()
