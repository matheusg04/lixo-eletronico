import requests
import time

LOCAL_API = "http://127.0.0.1:5000/points"
SEARCH_API = "http://127.0.0.1:5000/search"

# Lista oficial extraída do PDF (Pilhas e Baterias)
pontos_pilhas = [
    ("ATACADÃO CEASA", "R. Vítor Valpírio, 850, Porto Alegre", "Pilhas/Baterias"),
    ("BISTEK SUPERMERCADOS - DEPÓSITO CENTRAL", "Avenida das Indústrias, 1290, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA AUXILIADORA", "R. Eudoro Berlink, 750, Porto Alegre", "Pilhas/Baterias"),
    ("ELETRÔNICA ADILSONS", "R. 24 de Outubro, 1305, Porto Alegre", "Pilhas/Baterias"),
    ("ASSIST. TÉCNICA CEDILAR", "Av. Ipiranga, 1477, Porto Alegre", "Pilhas/Baterias"),
    ("PONTO FRIO AZENHA", "Av. Azenha, 855a, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA CASEMIRO DE ABREU", "R. Casemiro de Abreu, 1216, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA CAMAQUÃ", "Av. Otto Niemeyer, 2058, Porto Alegre", "Pilhas/Baterias"),
    ("PONTO FRIO CAVALHADA", "Avenida da Cavalhada, 2905, Porto Alegre", "Pilhas/Baterias"),
    ("CASAS BAHIA", "R. Dr. Flores, 75, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA ANDRADAS", "R. dos Andradas, 1195, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA DUQUE DE CAXIAS", "R. Duque de Caxias, 907, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 25", "Largo Visconde do Cairu, 17, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA TRISTEZA", "Av. Wenceslau Escobar, 2287, Porto Alegre", "Pilhas/Baterias"),
    ("KALUNGA CRISTAL", "Av. Diário de Notícias, 300, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA PASSO D'AREIA", "Av. Assis Brasil, 2127, Porto Alegre", "Pilhas/Baterias"),
    ("KALUNGA ASSIS BRASIL", "Av. Assis Brasil, 2611, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 23", "Avenida Assis Brasil, 3277, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA CRISTÓVÃO", "Av. Cristóvão Colombo, 2125, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA BOA VISTA", "Av. Cristóvão Colombo, 3701, Porto Alegre", "Pilhas/Baterias"),
    ("PANASUL ELETRONICA", "R. Álvaro Chaves, 431, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 40", "R. Visconde do Rio Branco, 566, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA RIO BRANCO", "R. Mostardeiro, 747, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA IPANEMA", "R. Eng. Coelho Parreira, 668, Porto Alegre", "Pilhas/Baterias"),
    ("CARREFOUR JARDIM BOTÂNICO", "R. Albion, 111, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA MENINO DEUS", "Av. Getúlio Vargas, 1685, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA BARÃO DE CERRO LARGO", "R. Barão de Cerro Largo, 212, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 26", "Av. Getulio Vargas, 1039, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA MOINHOS DE VENTO", "R. Dr. Florêncio Ygartua, 118, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA PEDRO IVO", "R. Pedro Ivo, 847, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA NONOAI", "R. Sepé Tiarajú, 1089, Porto Alegre", "Pilhas/Baterias"),
    ("CARREFOUR PASSO D'AREIA", "Av. Plínio Brasil Milano, 2343, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA JOÃO WALLIG", "Av. João Wallig, 1800, Porto Alegre", "Pilhas/Baterias"),
    ("KALUNGA JOÃO WALLIG", "Av. João Wallig, 1800, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA PETRÓPOLIS A", "R. Barão do Amazonas, 278, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA PETRÓPOLIS B", "Rua Amélia Teles, 470, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 22", "Avenida Carlos Gomes , 1657, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 32", "Av. Protásio Alves , 590, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA PRAIA DE BELAS", "Av. Praia de Belas, 1181, Porto Alegre", "Pilhas/Baterias"),
    ("KALUNGA PRAIA DE BELAS", "Av. Praia de Belas, 1181, Porto Alegre", "Pilhas/Baterias"),
    ("MULTICOISAS PRAIA DE BELAS", "Av. Praia de Belas, 1181, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA SANTANA", "R. Jerônimo de Ornelas, 241, Porto Alegre", "Pilhas/Baterias"),
    ("ATACADÃO SERTÓRIO", "Av. Sertório, 6767, Porto Alegre", "Pilhas/Baterias"),
    ("LEROY MERLIN SERTÓRIO", "Av. Sertório, 6767, Porto Alegre", "Pilhas/Baterias"),
    ("DROGA RAIA TRÊS FIGUEIRAS", "R. José Antônio Aranha, 423, Porto Alegre", "Pilhas/Baterias"),
    ("SICOOB CREDICAPITAL - 24", "Av. Wenceslau Escobar,1823, Porto Alegre", "Pilhas/Baterias"),
    ("BISTEK SUPERMERCADOS - LOJA 26", "Av. do Forte, 1396, Porto Alegre", "Pilhas/Baterias"),
]

print("\nIniciando seed de Pilhas/Baterias...\n")

for nome, end, tipo in pontos_pilhas:
    print(f"Geocodificando: {nome} — {end}")

    try:
        geo = requests.get(SEARCH_API, params={"q": end}, timeout=10).json()
    except Exception as e:
        print("  [ERRO] Falha de requisição:", e)
        continue

    if not geo or "error" in geo:
        print("  [ERRO] Não foi possível geocodificar. Pulando.")
        continue

    lat = float(geo[0]["lat"])
    lon = float(geo[0]["lon"])

    payload = {
        "name": nome,
        "address": end,
        "latitude": lat,
        "longitude": lon,
        "waste_type": tipo
    }

    r = requests.post(LOCAL_API, json=payload)

    if r.status_code == 201:
        print("  ✔ Inserido com sucesso!")
    else:
        print("  ✖ Erro ao inserir:", r.text)

    time.sleep(0.4)

print("\nSeed de Pilhas/Baterias finalizado.\n")
