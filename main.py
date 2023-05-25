import certifi
import json
import requests
import pandas as pd
import pathlib
from urllib.request import urlopen

API_KEY = "ec8aaad6454e843df5769f13438e4bb7"

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = f"https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey={API_KEY}"
print(get_jsonparsed_data(url))