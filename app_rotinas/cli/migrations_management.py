from subprocess import call

import click


path_ini_alembic_file = 'app_config/config_files/alembic.ini'


@click.group('db')
def db():
    ...


@db.command()
@click.option('-m', 'message', default='migração via CLI',
              help='Mensagem para identificar a migrations do alembic')
def makemigration(message):
    call(['alembic', '-c', path_ini_alembic_file, 'revision', '-m', message])


@db.command()
def migrate():
    call(['alembic', '-c', path_ini_alembic_file, 'upgrade', 'head'])


@db.command()
@click.option('-m', 'message', default='migração via CLI',
              help='Mensagem para identificar a migrations do alembic')
def initialize(message):
    ...
