# import requests
import json
import pandas as pd

def vanishPerc(series):
    new_list = []
    for value in series:
        if "%" in value:
            value_new = float(value.replace('%',''))/100
            new_list.append(value_new)
        else:
            new_list.append(value)
    return pd.Series(new_list)

def str2float(series):
    new_list = []
    for value in series:
        try:
            value_float = float(value)
            new_list.append(value_float)
        except:
            new_list.append(value)
    return pd.Series(new_list)


def vanishData(data):    
    # req = requests.get(localhost)

    data = json.loads(data)
    papel_name = list(data)
    papel_list = []

    for name in papel_name:
        papel = data[name]
        papel.update({"papel": name})
        papel_list.append(papel)

    df = pd.DataFrame(papel_list) 

    df = df.apply(lambda x: x.str.replace('.',''))
    df = df.apply(lambda x: x.str.replace(',','.'))
    df = df.apply(lambda x: x.str.replace(',','.'))
    df = df.apply(vanishPerc)
    df = df.apply(str2float)
    return df.to_json()