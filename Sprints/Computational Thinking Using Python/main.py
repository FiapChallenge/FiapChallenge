import json
from lib.commands import solicitar_guinho, listar_guinchos, contato, settings, config
import os

resumo_operacoes = []


def print_menu():
    menu = """
--------------------------
          Menu
0 - Sair
1 - Solicitar Guincho
2 - Listar Guinchos
3 - Contato
4 - Configurações
--------------------------
    """
    print(menu)


while __name__ == "__main__":
    print_menu()
    opcao = input("Digite a opção desejada: ")
    print()
    if config["clear_output"]:
        os.system("cls" if os.name == "nt" else "clear")
    try:
        opcao = int(opcao)
    except:
        print("Digite um número")
        continue
    match opcao:
        case 0:
            resumo_operacoes.append("Sair")
            json.dump(config, open("settings.json", "w"))
            print("Resumo das operações realizadas: ")
            for idx, operacao in enumerate(resumo_operacoes):
                print(f"{idx + 1} - {operacao}")
            exit()
        case 1:
            resumo_operacoes.append("Solicitar Guincho")
            solicitar_guinho(resumo_operacoes)
        case 2:
            resumo_operacoes.append("Listar Guinchos")
            listar_guinchos()
        case 3:
            resumo_operacoes.append("Contato")
            contato()
        case 4:
            resumo_operacoes.append("Configurações")
            settings(resumo_operacoes)
        case _:
            print("Opção inexistente")
