import json
import requests
import pandas as pd
import seaborn as sns


url = "https://covid19-brazil-api.now.sh/api/report/v1" 

headers = {
    'x-rapidapi-host': "covid19-brazil-api.now.sh/api/report/v1",
    'x-rapidapi-key': "KEY"
    }

response = requests.request("GET", url, headers=headers)
print(response)

parsed_data = json.loads(response.text)
print(parsed_data)
parsed_data


def flatten_json(json):
    dict1 = {}
    
    def flatten(i, name=""):
        if type(i) is dict:
            for a in i:
                flatten(i[a], name + a + '_')
        else:
            dict1[name[:-1]] = i
    
    flatten(json)
    return dict1

#Data Frame
dados = pd.DataFrame.from_dict(flatten_json(parsed_data),orient="index")
dados
