## Migrações

Após ser criado uma nova classe para o banco de dados digite o comando

`ensaio db -m "first migration" makemigration`

Em seguida

`ensaio db migrate`

## Executando o aplicativo

Para executar o aplicativo digite

`ensaio run app`

para abrir a documentação digite no navegador

`localhost:8000`

A porta padrão é 8000, para escolher outra porta digite

`ensaio run app -a 8080`

## Convertendo arquivos

Para converter um arquivo UI em arquivo py digite o comando

`ensaio file convert-ui -ui=arquivo_ui_sem_extensao -py=arquivo_py_sem_extensao`
