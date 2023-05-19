import json
from lib.commands import solicitar_guinho, listar_guinchos, contato, settings, config
import os
import re

resumo_operacoes = []
users = json.load(open("users.json", "r"))


def cadastro():
    print("Bem vindo ao sistema de guinchos!")
    opcao = input("Você já possui cadastro? (s/n): ")
    if opcao == "s":
        user = login()
        os.system("cls" if os.name == "nt" else "clear")
        return user
    elif opcao == "n":
        cadastrado = False
        while not cadastrado:
            nome = input("Digite seu nome: ").strip().capitalize()
            if len(nome) < 5:
                print("Nome muito curto")
                continue
            email = input("Digite seu email: ")
            # check if email is valid
            if not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email):
                print("Email inválido")
                continue
            if email in users:
                print("Email já cadastrado")
                continue
            senha = input("Digite sua senha: ")
            if " " in senha:
                print("Senha não pode conter espaços")
                continue
            if len(senha) < 5:
                print("Senha muito curta")
                continue
            users[email] = {"nome": nome, "email": email, "senha": senha}
            json.dump(users, open("users.json", "w"), indent=4)
            print("Cadastro realizado com sucesso")
            cadastrado = True
            return users[email]
    else:
        print("Opção inválida")
        cadastro()


def login():
    logged = False
    while not logged:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if email in users:
            if senha == users[email]["senha"]:
                print("Login realizado com sucesso")
                return users[email]
            else:
                print("Senha incorreta")
        else:
            print("Email não cadastrado")


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


if __name__ == "__main__":
    user = cadastro()
    if user is not None:
        print(f"Bem vindo {user['nome']}")
    while True:
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
                json.dump(users, open("users.json", "w"), indent=4)
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
