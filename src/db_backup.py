import click
from config.config import Config


@click.group()
def main():
    """
    DB Backup\n
    App allow to backup mysql database located in docker containers.
    """
    pass


@main.command('backup')
def backup_cmd():
    """Process backup. Put this command into cron"""
    print('process')


@main.command('config')
def config_cmd():
    """Config database connections"""
    config = Config()
    config.run()


if __name__ == '__main__':
    main()
