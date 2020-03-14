#!/usr/bin/env python3

from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime
import json
from vanish.main import vanishData

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')

@app.route("/original")
def original():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        return jsonify(lista)


@app.route("/tabela")
def table():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        data = json.dumps(lista)
        data = vanishData(data)
        return data
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        data = json.dumps(lista)
        data = vanishData(data)
        return data





app.run(debug=True)