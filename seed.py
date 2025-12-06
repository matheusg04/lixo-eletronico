import requests
data = [
  {"name":"EcoPonto Central","address":"Rua Principal, 123","latitude":-30.0346,"longitude":-51.2177,"waste_type":"Eletrônicos"},
  {"name":"Ponto Pilhas","address":"Av. Teste, 45","latitude":-30.0400,"longitude":-51.2100,"waste_type":"Pilhas"},
  {"name":"Ponto Óleo","address":"R. Verde, 10","latitude":-30.0300,"longitude":-51.2200,"waste_type":"Óleo"}
]
for p in data:
    r = requests.post("http://127.0.0.1:5000/points", json=p)
    print(r.status_code, r.json())
