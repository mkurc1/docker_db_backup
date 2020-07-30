import click
from config.config import Config
from backup.object_storage import ObjectStorage
from dotenv import load_dotenv
from tabulate import tabulate


@click.group()
def main():
    """
    DB Backup\n
    App allow to backup mysql database located in docker containers and send it into OVH Object Storage.
    """
    load_dotenv()


@main.command('backup')
def backup_cmd():
    """Process backup. Put this command into cron"""
    object_storage = ObjectStorage()

    result = object_storage.list(container="backup")
    print(tabulate(result, headers="keys"))


@main.command('config')
def config_cmd():
    """Config database connections"""
    config = Config()
    config.run()


if __name__ == '__main__':
    main()
