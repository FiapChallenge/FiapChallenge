import json
from lib.var_texts import categoria_tarifaria, categoria_tarifaria_importado, categoria_tarifaria_especial, guinchos, text_categoria_tarifaria


try:
    with open("settings.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"clear_output": False}


# with open("./lib/categoria.txt", "r", encoding="UTF-8") as f:
#     text_categoria_tarifaria = f.read()

def solicitar_guinho(resumo_operacoes):
    print("Opção escolhida: Solicitar Guincho")
    while True:
        try:
            cod_tarifa = input(
                "Digite a categoria tarifária -> (número do código) | (digite 'listar' para ver as categorias e 'cancelar' para cancelar a solicitação): "
            )
            if cod_tarifa == "listar":
                print(text_categoria_tarifaria)
                continue
            elif cod_tarifa == "cancelar":
                resumo_operacoes.append("Solicitação de guincho cancelada")
                break
            else:
                cod_tarifa = int(cod_tarifa)
        except ValueError:
            print("Digite um número válido")
            continue
        if (
            cod_tarifa in categoria_tarifaria.keys()
            or cod_tarifa in categoria_tarifaria_importado.keys()
            or cod_tarifa in categoria_tarifaria_especial.keys()
        ):
            if cod_tarifa in categoria_tarifaria.keys():
                print(
                    "\nCategoria tarifária escolhida (Nacional): ",
                    categoria_tarifaria[cod_tarifa],
                )
            elif cod_tarifa in categoria_tarifaria_importado.keys():
                print(
                    "\nCategoria tarifária escolhida (Importado): ",
                    categoria_tarifaria_importado[cod_tarifa],
                )
            elif cod_tarifa in categoria_tarifaria_especial.keys():
                print(
                    "\nCategoria tarifária escolhida (Especial): ",
                    categoria_tarifaria_especial[cod_tarifa],
                )
            endereco = input("Digite o endereço atual: ")
            # TODO - Implementar a busca de guinchos disponíveis e melhorar a busca, adicionar sistema de localização real e tempo de espera
            if cod_tarifa >= 93:
                print("Guincho escolhido:", guinchos[0])
            elif cod_tarifa > 80:
                print("Guincho escolhido:", guinchos[1])
            elif cod_tarifa > 70:
                print("Guincho escolhido:", guinchos[2])
            elif cod_tarifa > 60:
                print("Guincho escolhido:", guinchos[3])
            elif cod_tarifa > 50:
                print("Guincho escolhido:", guinchos[4])
            elif cod_tarifa > 40:
                print("Guincho escolhido:", guinchos[5])
            elif cod_tarifa > 30:
                print("Guincho escolhido:", guinchos[6])
            elif cod_tarifa > 20:
                print("Guincho escolhido:", guinchos[7])
            elif cod_tarifa >= 10:
                print("Guincho escolhido:", guinchos[8])
            print("Guincho indo para o local")
            resumo_operacoes.append(
                "Guincho escolhido: " + guinchos[0] + " para o endereço: " + endereco
            )
            break
        else:
            print("Categoria tarifária não encontrada")
            continue


def listar_guinchos():
    print("Opção escolhida: Listar Guinchos")
    print("Guinchos disponíveis: ")
    for guincho in guinchos:
        print(guincho)


def contato():
    print("Opção escolhida: Contato")
    print(
        """
Assistência pelo WhatsApp

55 11 3003 9303
Para pedir assistência, adicione o WhatsApp da Porto aos seus contatos e siga as orientações da nossa assistente virtual.

Central de serviços
Grande São Paulo: 333 76786
Capitais e regiões metropolitanas: 4004 76786
Demais localidades: 0300 337 6786
Aviso de sinistro, solicitação de serviços para automóvel, residência e outros. Atendimento 24h.

SAC
0800 727 2766
Atendimento 24h.

0800 727 8736
Atendimento exclusivo para pessoas com deficiência auditiva. De segunda a sexta-feira, das 6h às 22h.          
          """
    )


def settings(resumo_operacoes):
    for key, value in config.items():
        print(f"{key}: {value}")
    resposta = ""
    while resposta != "n":
        resposta = input("\nDesaja alterar alguma configuração? (s/n): ").lower()
        if resposta == "n":
            break
        elif resposta == "s":
            opcao = input("Digite o nome da configuração que deseja modificar: ")
            if opcao in config.keys():
                if opcao == "clear_output":
                    config[opcao] = not config[opcao]
                    resumo_operacoes.append(
                        f"Configuração alterada com sucesso | Novo valor de {opcao}: {config[opcao]}"
                    )
                    print(
                        f"Configuração alterada com sucesso | Novo valor de {opcao}: ",
                        config[opcao],
                    )
            else:
                print("Configuração inexistente")
        else:
            print("Opção inválida")

