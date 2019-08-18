from os import sep
from subprocess import call

import click


@click.group('run')
def run():
    ...


@run.command()
def app():
    """Executar a aplicação."""
    call([
        'python',
        'app_source' + sep + 'screens' + sep + 'gui_py' + sep + 'menu.py'
    ])


@run.command()
@click.option('-p', 'port', help='Escolher porta HTTP')
def documentation(port):
    if port:
        call(['mkdocs', 'serve', '-a', 'localhost:' + port])
        return

    call(['mkdocs', 'serve'])
