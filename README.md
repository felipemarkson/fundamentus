# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os 
principais indicadores fundamentalistas em formato JSON.

A API utiliza o microframework Flask.

Também é possível utilizar via linha de comando.

Para lidar com dados em programas de planilhas, como Excel ou Google Sheets, utilizar a API original.

Para lidar com Pandas, utilizar a API baseada em tabelas.

## Requisitos

[Python 3](https://www.python.org/)

[Poetry](http://python-poetry.org/)

## Instalação

    $ poetry install

## Linha de comando

### Original

    $ python3 fundamentus.py

### Tabela

    $ python3 fundamentus-tabela.py


## API
    $ python3 server.py

### Endpoints (GET):

* original : retorna os dados não tratados da API [original](https://github.com/phoemur/fundamentus). A resposta trará cada papel como um objeto e indicadores como propriedades de cada objeto. Os valores não estão tratados para uso direto em python. Ex:

```json
  "BRFS3": {
    "Cresc.5a": "2,36",
    "DY": "0,00%",
    "ROIC": "1,13",
    "cotacao": "16,49"
  }
```

* tabela: retorna um JSON preparado para tratamento utilizando Pandas. Os valores estão tratados para uso direto em python com [pandas.DataFrame()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) Ex:

```python
import requests
import json
import pandas as pd

localhost =  "http://127.0.0.1:5000/"
res = requests.get(localhost+"tabela")
data_json = json.loads(req.content)
df = pd.DataFrame(data_json)
```
Na resposta da API baseada em tabelas o nome do papel é mais atributo.




