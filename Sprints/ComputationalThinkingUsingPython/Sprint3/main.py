# Sprint #3: Preparação dos dados para IA

# A partir da base dados adotada nas outras disciplinas, a equipe deverá desenvolver um programa  em Python, o qual deverá contemplar os seguintes itens:
# [35 pts] os dados deverão ser filtrados e armazenados em listas de dicionários;
# [35 pts] tratamento de erros para a inserção e alteração dos dados (If e else);
# [30 pts] menu com submenus para acesso aos dados.

# Entregáveis:
# Arquivo .zip com os arquivos do projeto do Python.
# Arquivo .txt com as explicações e nomes dos membros do grupo.

import csv
import json
import os
import utils.comandos as comandos


def load_data():
    if os.path.isfile("data/modelos.json"):
        with open("data/modelos.json", "r", encoding="utf8") as f:
            modelos_data = json.load(f)
        return modelos_data

    marcas_data = {}
    # https://www.luiztools.com.br/post/base-de-dados-com-todas-as-marcas-e-modelos-de-veiculos/ - Marcas e modelos de veículos
    with open(
        "Database/marcas-carros.csv", "r", newline="", encoding="utf-8-sig"
    ) as marca_file:
        marca_reader = csv.DictReader(marca_file, delimiter=";")
        for row in marca_reader:
            marcas_data[int(row["ID"])] = row["NOME"]

    with open(
        "Database/marcas-caminhao.csv", "r", newline="", encoding="utf-8-sig"
    ) as marca_file:
        marca_reader = csv.DictReader(marca_file, delimiter=";")
        for row in marca_reader:
            marcas_data[int(row["ID"])] = row["NOME"]

    with open(
        "Database/marcas-motos.csv", "r", newline="", encoding="utf-8-sig"
    ) as marca_file:
        marca_reader = csv.DictReader(marca_file, delimiter=";")
        for row in marca_reader:
            marcas_data[int(row["ID"])] = row["NOME"]

    # Read the 'modelos.csv' file into a list of dictionaries
    modelos_data = []
    with open(
        "Database/modelos-carro.csv", "r", newline="", encoding="utf-8-sig"
    ) as modelo_file:
        modelo_reader = csv.DictReader(modelo_file, delimiter=";")
        for row in modelo_reader:
            modelos_data.append(
                {
                    "ID": int(row["ID"]),
                    "MARCA": marcas_data[int(row["IDMARCA"])],
                    "NOME": row["NOME"],
                    "TIPO": "Carro",
                }
            )

    with open(
        "Database/modelos-caminhao.csv", "r", newline="", encoding="utf-8-sig"
    ) as modelo_file:
        modelo_reader = csv.DictReader(modelo_file, delimiter=";")
        for row in modelo_reader:
            modelos_data.append(
                {
                    "ID": int(row["ID"]),
                    "MARCA": marcas_data[int(row["IDMARCA"])],
                    "NOME": row["NOME"],
                    "TIPO": "Caminhão",
                }
            )

    with open(
        "Database/modelos-moto.csv", "r", newline="", encoding="utf-8-sig"
    ) as modelo_file:
        modelo_reader = csv.DictReader(modelo_file, delimiter=";")
        for row in modelo_reader:
            modelos_data.append(
                {
                    "ID": int(row["ID"]),
                    "MARCA": marcas_data[int(row["IDMARCA"])],
                    "NOME": row["NOME"],
                    "TIPO": "Moto",
                }
            )

    modelos_data.sort(key=lambda x: x["ID"])

    for i, modelo in enumerate(modelos_data):
        modelo["ID"] = i

    return modelos_data


def print_menu():
    menu = """
--------------------------
          Menu
0 - Sair
1 - Listagem de modelos
2 - Inserir modelo
3 - Alterar modelo
4 - Excluir modelo
5 - Configurações
--------------------------
"""
    print(menu)


if __name__ == "__main__":
    modelos_data = load_data()
    while True:
        print_menu()
        option = int(input("Digite a opção desejada: "))
        if comandos.config["clear_output"]:
            os.system("cls" if os.name == "nt" else "clear")
        match option:
            case 0:
                break
            case 1:
                comandos.listar_modelos_submenu(modelos_data)
            case 2:
                comandos.inserir_modelo(modelos_data)
            case 3:
                comandos.alterar_modelo(modelos_data)
            case 4:
                comandos.excluir_modelo(modelos_data)
            case 5:
                comandos.configuracoes()
            case _:
                print("Opção inválida")
