import json
import os
from tabulate import tabulate
from modelos_crud import ModelosCRUD


try:
    with open("data/settings.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"clear_output": False, "sort_by": "ID"}


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
                if opcao == "sort_by":
                    print("Opções de ordenação: ")
                    print("1 - ID")
                    print("2 - Nome")
                    print("3 - Marca")
                    print("4 - Tipo")
                    opcao = input("Digite a opção desejada: ")
                    if opcao == "1":
                        config["sort_by"] = "ID"
                    elif opcao == "2":
                        config["sort_by"] = "NOME"
                    elif opcao == "3":
                        config["sort_by"] = "MARCA"
                    elif opcao == "4":
                        config["sort_by"] = "TIPO"
                    else:
                        print("Opção inválida")
                    json.dump(
                        config,
                        open("data/settings.json", "w", encoding="utf8"),
                        indent=4,
                    )
                    print(
                        f"Configuração alterada com sucesso | Novo valor de sort_by: {config['sort_by']}"
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


def listar_modelos_submenu():
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
        data = ModelosCRUD.get_all_modelos(sort_by=config["sort_by"])
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
                modelos = ModelosCRUD.get_modelos_by_tipo(
                    modelo_tipo=tipo.capitalize(), sort_by=config["sort_by"]
                )
                print(tabulate(modelos, headers="keys", tablefmt="psql"))
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
                modelos = ModelosCRUD.get_modelos_by_marca(
                    modelo_marca=marca, sort_by=config["sort_by"]
                )
                print(tabulate(modelos, headers="keys", tablefmt="psql"))
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
                tabela = ModelosCRUD.get_modelos_by_tipo_marca(
                    modelo_tipo=tipo.capitalize(),
                    modelo_marca=marca,
                    sort_by=config["sort_by"],
                )
                if len(tabela) == 0:
                    print("Não há modelos com essa marca e tipo")
                    continue
                print(tabulate(tabela, headers="keys", tablefmt="psql"))
            case _:
                print("Opção inválida")


def buscar_modelo():
    print("Opção escolhida: Buscar modelo")
    id = input("Digite o ID do modelo: ")
    if id.isnumeric():
        modelo = ModelosCRUD.get_modelo_by_id(modelo_id=int(id))
        if modelo:
            print(
                tabulate(
                    [
                        {
                            "ID": modelo["ID"],
                            "NOME": modelo["NOME"],
                            "MARCA": modelo["MARCA"],
                            "TIPO": modelo["TIPO"],
                        }
                    ],
                    headers="keys",
                    tablefmt="psql",
                )
            )
        else:
            print("ID não encontrado")


def inserir_modelo():
    data = ModelosCRUD.get_all_modelos()
    print("Opção escolhida: Inserir modelo")
    modelo = {}
    modelo["ID"] = input(
        "Digite o ID do modelo (vazio para adicionar 1 ao último registrado): "
    )
    if modelo["ID"] == "":
        modelo["ID"] = str(sorted(data, key=lambda x: x["ID"])[-1]["ID"] + 1)
        print(f"ID gerado: {modelo['ID']}")
    if not modelo["ID"].isnumeric():
        print("ID inválido")
        return
    if int(modelo["ID"]) in [modelo["ID"] for modelo in data]:
        print("ID já cadastrado")
        return
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

    ModelosCRUD.create_modelo(
        id=modelo["ID"],
        nome=modelo["NOME"],
        marca=modelo["MARCA"],
        tipo=modelo["TIPO"],
    )
    print("Modelo inserido com sucesso")
    option = input("Deseja inserir outro modelo? (s/n): ").lower()
    if option == "s":
        print()
        inserir_modelo()


def alterar_modelo():
    print("Opção escolhida: Alterar modelo")
    data = ModelosCRUD.get_all_modelos()
    print(tabulate(data, headers="keys", tablefmt="psql"))
    print()
    idStr = input("Digite o ID do modelo que deseja alterar: ")
    if not idStr.isnumeric():
        print("ID inválido")
        return
    id = int(idStr)
    if id in [modelo["ID"] for modelo in data]:
        ModelosCRUD.update_modelo(
            modelo_id=id,
            nome=input("Digite o novo nome do modelo: "),
            marca=input("Digite a nova marca do modelo: ").upper(),
            tipo=input("Digite o novo tipo do modelo: ").capitalize(),
        )
    else:
        print("ID inválido")


def excluir_modelo():
    print("Opção escolhida: Excluir modelo")
    data = ModelosCRUD.get_all_modelos()
    print(tabulate(data, headers="keys", tablefmt="psql"))
    print()
    idStr = input("Digite o ID do modelo que deseja excluir: ")
    if not idStr.isnumeric():
        print("ID inválido")
        return
    id = int(idStr)
    if id in [modelo["ID"] for modelo in data]:
        ModelosCRUD.delete_modelo(modelo_id=id)
        print("Modelo excluído com sucesso")
    else:
        print("ID inválido")
