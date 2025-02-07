from click import group

from app_rotinas.cli.migrations_management import db
from app_rotinas.cli.convert_ui_files import file


@group('cli')
def cli():
    ...


cli.add_command(db)
cli.add_command(file)

cli()
