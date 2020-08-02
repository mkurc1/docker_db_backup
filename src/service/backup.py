import tempfile

from .db_dumper import DbDumper
from .object_storage import ObjectStorage
from .db_connector import DbConnector


class Backup:
    def __init__(self):
        self.__db_dumper = DbDumper()
        self.__db_connector = DbConnector('config', 'config')
        self.__object_storage = ObjectStorage()

    def process(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            for (row_id, container, root_pass, db_name) in self.__db_connector.list():
                try:
                    (file_path, file_name) = self.__db_dumper.dump(tmp_dir, container, root_pass, db_name)
                except FileNotFoundError:
                    continue
                self.__object_storage.upload('backup', file_path, file_name)
