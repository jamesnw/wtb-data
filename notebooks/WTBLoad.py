import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
import json

def load():
    url = "http://whattobrew.com/data/data_export.json"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    contents = urlopen(req).read()
    data = json.loads(contents.decode('utf-8'))

    return pd.read_json(contents)

def load_frame():
    df = load()
    x = df.unstack().to_frame()
    x.reset_index(inplace=True)
    x.rename(columns={'level_0':'addition','level_1':'style',0:'vote'}, inplace=True)
    return x