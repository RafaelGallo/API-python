import requests
import json
import csv
from acesso_cep import BuscaEndereco

cep = "02265001"
objeto_cep = BuscaEndereco(cep)

r = requests.get("https://viacep.com.br/ws/02265001/json/")
print(r.text)

