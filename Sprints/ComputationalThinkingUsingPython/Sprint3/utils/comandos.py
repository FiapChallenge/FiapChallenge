import json
import csv
import os
from tabulate import tabulate

try:
    with open("data/settings.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"clear_output": False}


def configuracoes():
    print("Opção escolhida: Configurações")
    for key, value in config.items():
        print((f"{key}: {value}"))
    resposta = ""
    while resposta != "n":
        resposta = input(("\nDeseja alterar alguma configuração? (s/n): ")).lower()
        if resposta == "n":
            break
        elif resposta == "s":
            opcao = input(("Digite o nome da configuração que deseja modificar: "))
            if opcao in config.keys():
                if type(config[opcao]) == bool:
                    config[opcao] = not config[opcao]
                    print(
                        f"Configuração alterada com sucesso | Novo valor de {opcao}: ",
                        config[opcao],
                    )
                    json.dump(
                        config,
                        open("data/settings.json", "w", encoding="utf8"),
                        indent=4,
                    )
            else:
                print("Configuração inexistente")
        else:
            print("Opção inválida")


def listar_opcoes(data, chave, tipo=None):
    if tipo == None:
        opcoes = list(set([modelo[chave] for modelo in data]))
    else:
        opcoes = list(
            set([modelo[chave] for modelo in data if modelo["TIPO"].lower() == tipo])
        )
    opcoes.sort()
    print(
        tabulate(
            [opcoes[i : i + 5] for i in range(0, len(opcoes), 5)], tablefmt="pretty"
        )
    )
    print()


def listar_modelos_submenu(data):
    while True:
        menu = """
------------------------------------
         Listagem
0 - Voltar
1 - Listar todos os modelos
2 - Listar modelos por tipo
3 - Listar modelos por marca
4 - Listar modelos por tipo e marca
------------------------------------
          
        """
        print(menu)
        option = int(input("Digite a opção desejada: "))
        if config["clear_output"]:
            os.system("cls" if os.name == "nt" else "clear")
        match option:
            case 0:
                return
            case 1:
                print(tabulate(data, headers="keys", tablefmt="psql"))
            case 2:
                tipo = input(
                    "Digite o tipo do modelo (digite lista para ver os disponiveis): "
                ).lower()
                if tipo == "lista":
                    listar_opcoes(data, "TIPO")
                    tipo = input("Digite o tipo do modelo: ").lower()
                if tipo not in [modelo["TIPO"].lower() for modelo in data]:
                    print("Tipo inválido")
                    continue
                print(
                    tabulate(
                        [modelo for modelo in data if modelo["TIPO"].lower() == tipo],
                        headers="keys",
                        tablefmt="psql",
                    )
                )
            case 3:
                marca = input(
                    "Digite a marca do modelo (digite lista para ver os disponiveis): "
                ).upper()
                if marca == "LISTA":
                    listar_opcoes(data, "MARCA")
                    marca = input("Digite a marca do modelo: ").upper()
                if marca not in [modelo["MARCA"] for modelo in data]:
                    print("Marca inválida")
                    continue
                print(
                    tabulate(
                        [modelo for modelo in data if modelo["MARCA"] == marca],
                        headers="keys",
                        tablefmt="psql",
                    )
                )
            case 4:
                tipo = input(
                    "Digite o tipo do modelo (digite lista para ver os disponiveis): "
                ).lower()
                if tipo == "lista":
                    listar_opcoes(data, "TIPO")
                    tipo = input("Digite o tipo do modelo: ").lower()
                if tipo not in [modelo["TIPO"].lower() for modelo in data]:
                    print("Tipo inválido")
                    continue
                marca = input(
                    "Digite a marca do modelo (digite lista para ver os disponiveis): "
                ).upper()
                if marca == "LISTA":
                    listar_opcoes(data, "MARCA", tipo)
                    marca = input("Digite a marca do modelo: ").upper()
                if marca not in [modelo["MARCA"] for modelo in data]:
                    print("Marca inválida")
                    continue
                tabela = [
                    modelo
                    for modelo in data
                    if modelo["TIPO"].lower() == tipo and modelo["MARCA"] == marca
                ]
                if len(tabela) == 0:
                    print("Não há modelos com essa marca e tipo")
                    continue
                print(tabulate(tabela, headers="keys", tablefmt="psql"))
            case _:
                print("Opção inválida")


def inserir_modelo(data):
    print("Opção escolhida: Inserir modelo")
    modelo = {}
    modelo["ID"] = len(data)
    modelo["MARCA"] = input("Digite a marca do modelo: ").upper()
    if ";" in modelo["MARCA"]:
        print("O caractere ';' é inválido")
        return
    if modelo["MARCA"] == "":
        print("A marca não pode ser vazia")
        return
    modelo["NOME"] = input("Digite o nome do modelo: ")
    if ";" in modelo["NOME"]:
        print("O caractere ';' é inválido")
        return
    if modelo["NOME"] == "":
        print("O nome não pode ser vazio")
        return
    modelo["TIPO"] = input("Digite o tipo do modelo: ").capitalize()
    if ";" in modelo["TIPO"]:
        print("O caractere ';' é inválido")
        return
    if modelo["TIPO"] == "":
        print("O tipo não pode ser vazio")
        return
    data.append(modelo)
    print("Modelo inserido com sucesso")
    save_data(data)
    option = input("Deseja inserir outro modelo? (s/n): ").lower()
    if option == "s":
        print()
        inserir_modelo(data)


def alterar_modelo(data):
    print("Opção escolhida: Alterar modelo")
    print(tabulate(data, headers="keys", tablefmt="psql"))
    print()
    idStr = input("Digite o ID do modelo que deseja alterar: ")
    if not idStr.isnumeric():
        print("ID inválido")
        return
    id = int(idStr)
    if id in [modelo["ID"] for modelo in data]:
        modelo = [modelo for modelo in data if modelo["ID"] == id][0]
        print("Modelo encontrado")
        print(tabulate([modelo], headers="keys", tablefmt="psql"))
        print()
        modelo["MARCA"] = input("Digite a marca do modelo: ").upper()
        modelo["NOME"] = input("Digite o nome do modelo: ")
        modelo["TIPO"] = input("Digite o tipo do modelo: ").capitalize()
        print("Modelo alterado com sucesso")
        save_data(data)
    else:
        print("ID inválido")


def excluir_modelo(data):
    print("Opção escolhida: Excluir modelo")
    print(tabulate(data, headers="keys", tablefmt="psql"))
    print()
    idStr = input("Digite o ID do modelo que deseja excluir: ")
    if not idStr.isnumeric():
        print("ID inválido")
        return
    id = int(idStr)
    if id in [modelo["ID"] for modelo in data]:
        data = [modelo for modelo in data if modelo["ID"] != id]
        print("Modelo excluído com sucesso")
        save_data(data)
    else:
        print("ID inválido")


def save_data(data):
    if config["create_csv"]:
        with open("data/modelos.csv", "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=";")
            writer.writeheader()
            writer.writerows(data)
    with open("data/modelos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
