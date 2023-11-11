# Tendo como referência o entregável da sprint 3, a equipe deverá desenvolver o CRUD em tabelas do BD Oracle em um programa em Python. Para tanto, os requisitos são os seguintes:

# [35pts] menus e submenus para acesso às opções do CRUD (insert, update, delete e select);
# [40 pts] pelos menos 2 relatórios com filtros (Select.... where).
# [25 pts] As informações colhidas e/ou alteradas pelo programa desenvolvido devem refletir no sistema web e vice-versa.

# Entregáveis:

# Arquivo .zip com os arquivos do projeto do Python e scripts do BD.

# Arquivo .txt com as explicações e nomes dos membros do grupo.

import os
import utils.comandosDB as comandosDB


def print_menu():
    menu = """
--------------------------
          Menu
0 - Sair
1 - Listagem de modelos
2 - Buscar modelo
3 - Inserir modelo
4 - Alterar modelo
5 - Excluir modelo
6 - Configurações
--------------------------
"""
    print(menu)


if __name__ == "__main__":
    while True:
        print_menu()
        option_int = input("Digite a opção desejada: ")
        if option_int.isnumeric():
            option = int(option_int)
        else:
            print("Digite um número")
            continue
        option = int(option_int)
        if comandosDB.config["clear_output"]:
            os.system("cls" if os.name == "nt" else "clear")
        match option:
            case 0:
                break
            case 1:
                comandosDB.listar_modelos_submenu()
            case 2:
                comandosDB.buscar_modelo()
            case 3:
                comandosDB.inserir_modelo()
            case 4:
                comandosDB.alterar_modelo()
            case 5:
                comandosDB.excluir_modelo()
            case 6:
                comandosDB.configuracoes()
            case _:
                print("Opção inválida")
