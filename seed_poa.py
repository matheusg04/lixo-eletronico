import requests
import time

LOCAL_API = "http://127.0.0.1:5000/points"

pontos = [
    {
        "name": "EcoPonto Conceição",
        "address": "Rua Alberto Bins, 650, Porto Alegre",
        "latitude": -30.027205,
        "longitude": -51.223266,
        "waste_type": "Eletrônicos"
    },
    {
        "name": "Ecoponto Câncio Gomes",
        "address": "Travessa Carmem, 111, Porto Alegre",
        "latitude": -30.022875,
        "longitude": -51.210784,
        "waste_type": "Eletrônicos"
    },
    {
        "name": "Ecoponto Glória",
        "address": "Rua Professor Carvalho de Freitas, 1012, Porto Alegre",
        "latitude": -30.065156,
        "longitude": -51.170538,
        "waste_type": "Eletrônicos"
    },
    {
        "name": "Ecoponto Humaitá",
        "address": "Rua José Aloísio Filho, 780, Porto Alegre",
        "latitude": -29.980556,
        "longitude": -51.224031,
        "waste_type": "Eletrônicos"
    },
    {
        "name": "Ecoponto Cruzeiro",
        "address": "Av. Cruzeiro do Sul, 1445, Porto Alegre",
        "latitude": -30.075705,
        "longitude": -51.227350,
        "waste_type": "Eletrônicos"
    },
    {
        "name": "Ecoponto Princesa Isabel",
        "address": "Av. Ipiranga, 2765, Porto Alegre",
        "latitude": -30.046631,
        "longitude": -51.197312,
        "waste_type": "Eletrônicos"
    },
]

print("Inserindo pontos reais de Porto Alegre...\n")

for p in pontos:
    print(f"Inserindo: {p['name']}")
    r = requests.post(LOCAL_API, json=p)
    if r.status_code == 201:
        print("  -> Inserido com sucesso!")
    else:
        print("  -> Erro ao inserir:", r.text)

    time.sleep(0.3)

print("\nFinalizado! Atualize o mapa.")
