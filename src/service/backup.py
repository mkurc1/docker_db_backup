import os

from .db_dumper import DbDumper
from .object_storage import ObjectStorage
from .db_connector import DbConnector


class Backup:
    def __init__(self, dump_dir):
        self.__db_dumper = DbDumper(dump_dir)
        self.__db_connector = DbConnector('config', 'config')

        config = {
            "auth_version": 3,
            "os_username": os.environ.get('OBJECT_STORAGE_USERNAME'),
            "os_password": os.environ.get('OBJECT_STORAGE_PASSWORD'),
            "os_project_name": os.environ.get('OBJECT_STORAGE_PROJECT_NAME'),
            "os_project_domain_name": os.environ.get('OBJECT_STORAGE_PROJECT_DOMAIN_NAME'),
            "os_auth_url": os.environ.get('OBJECT_STORAGE_AUTH_URL'),
            "os_region_name": os.environ.get('OBJECT_STORAGE_REGION'),
        }
        self.__object_storage = ObjectStorage(config)

    def process(self):
        for (row_id, container, root_pass, db_name) in self.__db_connector.list():
            try:
                (file_path, file_name) = self.__db_dumper.dump(container, root_pass, db_name)
            except FileNotFoundError:
                continue
            self.__object_storage.upload('backup', file_path, file_name)
            os.system(f'rm {file_path}')
