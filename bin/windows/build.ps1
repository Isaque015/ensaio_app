###############
#
#  Script para configurar o ambiente do projeto
#  Dependências
#  Make, pip, git
#
###############

# pip install pipenv
# pipenv install
#
# python setup.py install

$path = "app_rotinas\migrations\versions"

$pastaMigrations = Get-ChildItem $path
$pastaMigrations.count
# $pastaMigrations.GetFiles();


# $verificar_pasta_vazia = $(ls $PASTA_MIGRATIONS | wc -l)
#
# if [ $verificar_pasta_vazia -gt 1 ]; then
#     ensaio db makemigration
# fi
#
# ensaio db migrate
