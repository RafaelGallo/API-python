import requests
from clima import clima_API

clima = clima_API
r1 = requests.get("http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a954d7f6fd425daba5fe25ec979f8d9f")
r2 = requests.get("https://api.hgbrasil.com/weather?key=e1a836da&lat=-23.682&log=-46.875&user_ip=remote")

print(r1.text)
print("\n")
print(r2.text)