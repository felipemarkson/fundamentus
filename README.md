# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os 
principais indicadores fundamentalistas em formato JSON.
A API utiliza o microframework Flask.
Também é possível utilizar via linha de comando.

# Instalação
    $ poetry install

# Linha de comando (Original)
    $ python3 fundamentus.py

# API
    $ python3 server.py

Endpoints (GET):

    * /original : retorna os dados não tratados da API [original](https://github.com/phoemur/fundamentus)

    * /table: retorna um JSON preparado para tratamento utilizando Pandas, através do comando:  $ pandas.DataFrame()

# Requirements
    Poetry (https://python-poetry.org/)


