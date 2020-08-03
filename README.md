# Docker Database Backup

It's CLI app which allow to backup mysql database located in docker containers and send it into Object Storage. This app required to work Python 3.7, pip3 and pipenv.

## Install

Pull app from docker

```shell script
$ git clone git@github.com:mkurc1/docker_db_backup.git
```

Enter into directory

```shell script
$ cd docker_db_backup
```

Create .env file and update data Object Storage configuration

```shell script
$ cp .env.dist .env
```

Install dependencies

```shell script
$ pipenv install
```

Adds cron config (For example once a day at 3:30 am)

```
30 3 * * * cd /<PATH>/docker_db_backup && pipenv run python src/db_backup.py backup
```

## Commands

```
add     Add new connection
backup  Process backup
edit    Edit exist connection
list    List of all database connections
remove  Remove exist connection
```

You can check list of comments by execute:

```shell script
$ pipenv run python src/db_backup.py
``` 

## Configuration

Adds your docker containers name or id into configuration

```shell script
$ pipenv run python src/db_backup.py add
```  

## License

The App is released under the [MIT License](LICENSE).
