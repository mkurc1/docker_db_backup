import os
import subprocess
from datetime import datetime


class DbDumper:
    def dump(self, dump_dir, container, root_pass, db_name):
        file_name = f'{self.__prepare_file_name(db_name)}.sql.gz'
        file_path = f'{dump_dir}/{file_name}'

        cmd = f"docker exec {container} /usr/bin/mysqldump -uroot -p'{root_pass}' {db_name} " \
              f"| gzip -c > {file_path}"

        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = process.communicate()[1]

        if 'Error:' in str(stderr.strip()):
            os.system(f'rm {file_path}')
            raise FileNotFoundError(f'Dump database `{db_name}` from container `{container}` went wrong.')

        return file_path, file_name

    @staticmethod
    def __prepare_file_name(name):
        now = datetime.now()
        return f'{name.lower()}_{now.strftime("%d_%m_%Y-%H_%M_%S")}'
