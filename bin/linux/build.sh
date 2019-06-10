#!/bin/zsh

###############
#
#  Script para configurar o ambiente do projeto
#  Dependências
#  Make, pip, git
#
###############

pip install pipenv
pipenv install

python setup.py install

PASTA_MIGRATIONS="app_rotinas/migrations/versions"

VERIFICAR_PASTA_VAZIA = $(ls $PASTA_MIGRATIONS | wc -l)

if [ VERIFICAR_PASTA_VAZIA -le 1 ]; then
    ensaio db makemigration
fi

ensaio db migrate
