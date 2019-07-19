from os import sep
from subprocess import call

import click


@click.group('file')
def file():
    ...


@file.command()
@click.option('-ui', 'ui', help='Nome do arquivo ui')
@click.option('-py', 'py', help='Nome do arquivo py')
def convert_ui(ui, py):

    path_screens = 'app_source' + sep + 'screens' + sep

    file_ui = path_screens + ui + '.ui'
    file_py = path_screens + py + '.py'

    call(['pyside2-uic', file_ui, '>', file_py])
