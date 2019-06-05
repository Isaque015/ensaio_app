from click import group

from app_rotinas.cli.migrations_management import db


@group('cli')
def cli():
    ...


cli.add_command(db)

cli()
