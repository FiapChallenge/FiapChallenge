import json
import os

try:
    with open("settings.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {"clear_output": False}

resumo_operacoes = []
guinchos = [
    "GUINCHO PESADO NAO PADRAO",
    "PESADO COM PLAT HIDRAULICA MUNCK",
    "PESADO COM PLATAFORMA HIDRAULICA",
    "PESADO COM PLATAFORMA HIDRAULICA E BAND",
    "PESADO COM QUINTA RODA E BANDEJA",
    "PESADO COM TORRE E LANCA",
    "PESADO COM PLATAFORMA HIDRAULICA",
    "PESADO COM PLATAFORMA HIDRAULICA E LANCA",
    "PESADO COM QUINTA RODA E LANCA",
]

categoria_tarifaria = {
    10: "PASSEIO",
    14: "PICK- UP’S LEVES",
    16: "ESPORTIVOS",
    18: "MODELOS ESPECIAIS (PASSEIO)",
    20: "PICK- UP’S PESADAS - CARGA: FORD: F100, F1000 e RANGER (Cabine Simples ou Supercab) GM: ACD/10 e 20 , SILVERADO e S10 (Cabine Simples ou Estendida) TOYOTA PICK- UP E DODGE DAKOTA (Cabine Simples)",
    20: "PICK- UP’S PESADAS - PESSOAS: FORD: F100, F1000, F250 e RANGER (Cabine Dupla) GM: ACD/10 e 22 S10 e SILVERADO (Cabine Dupla), BONANZA, S10 BLAZER e VERANEIO. TOYOTA JEEP e GURGEL CARAJÁS DODGE DAKOTA CLUB CAB (Cabine Estendida) DERIVADAS DE PICK- UP PESADAS FORD e GM",
    30: "BICICLETAS MOTORIZADAS, MOTOCICLETAS, MOTONETAS COM REBOQUE OU “SIDE- CAR”, VEÍCULOS “ROMI- ISETTA” e VESPACAR.",
    40: "CAMINHÕES LEVES (PBT até 40 toneladas)",
    42: "CAMINHÕES PESADOS (PBT* acima de 42 toneladas, inclusive)",
    50: "REBOCADORES",
    52: "REBOQUES E SEMI- REBOQUES",
    58: "ÔNIBUS E MICROÔNIBUS COM COBRANÇA DE FRETE (exceto urbano com linha regular)",
    60: "ÔNIBUS, MICROÔNIBUS COM COBRANÇA DE FRETE (urbano com linha regular)",
    62: "ÔNIBUS, MICROÔNIBUS SEM COBRANÇA DE FRETE",
    68: "TRATORES E MÁQUINAS DE USO URBANO",
    70: "TRATORES E MÁQUINAS DE USO RURAL",
    72: "GUINCHOS (carro socorro)",
    80: "TÁXI",
    82: "LOTAÇÃO",
    84: "VEÍCULO ESCOLAR (transporte escolar)",
    88: "VIAGEM DE ENTREGA DENTRO DO TERRITÓRIO NACIONAL",
    89: "VIAGEM DE ENTREGA EXCLUSIVAMENTE PARA PAÍSES DA AMÉRICA DO SUL",
    90: "LOCADORAS",
    92: "VEÍCULOS FUNERÁRIOS",
}

categoria_tarifaria_importado = {
    11: "PASSEIO",
    15: "PICK- UP’S LEVES",
    17: "ESPORTIVOS",
    19: "MODELOS ESPECIAIS (PASSEIO)",
    21: "PICK- UP’S PESADAS - CARGA: FORD: F100, F1000 e RANGER (Cabine Simples ou Supercab) GM: ACD/10 e 20, SILVERADO e S10 (Cabine Simples ou Estendida) TOYOTA PICK- UP E DODGE DAKOTA (Cabine Simples)",
    23: "PICK- UP’S PESADAS - PESSOAS: FORD: F100, F1000, F250 e RANGER (Cabine Dupla) GM: ACD/10 e 20, S10 e SILVERADO (Cabine Dupla), BONANZA, S10 BLAZER e VERANEIO. TOYOTA JEEP e GURGEL CARAJÁS DODGE DAKOTA CLUB CAB (Cabine Estendida) DERIVADAS DE PICK- UP PESADAS FORD e GM",
    31: "BICICLETAS MOTORIZADAS, MOTOCICLETAS, MOTONETAS COM REBOQUE OU “SIDE- CAR”, VEÍCULOS “ROMI- ISETTA” e VESPACAR.",
    41: "CAMINHÕES LEVES (PBT até 10 toneladas)",
    43: "CAMINHÕES PESADOS (PBT* acima de 10 toneladas, inclusive)",
    51: "REBOCADORES",
    53: "REBOQUES E SEMI- REBOQUES",
    59: "ÔNIBUS E MICROÔNIBUS COM COBRANÇA DE FRETE (exceto urbano com linha regular)",
    61: "ÔNIBUS, MICROÔNIBUS COM COBRANÇA DE FRETE (urbano com linha regular)",
    63: "ÔNIBUS, MICROÔNIBUS SEM COBRANÇA DE FRETE",
    69: "TRATORES E MÁQUINAS DE USO URBANO",
    71: "TRATORES E MÁQUINAS DE USO RURAL",
    73: "GUINCHOS (carro socorro)",
    81: "TÁXI",
    83: "LOTAÇÃO",
    85: "VEÍCULO ESCOLAR (transporte escolar)",
    88: "VIAGEM DE ENTREGA DENTRO DO TERRITÓRIO NACIONAL",
    89: "VIAGEM DE ENTREGA EXCLUSIVAMENTE PARA PAÍSES DA AMÉRICA DO SUL",
    91: "LOCADORAS",
    93: "VEÍCULOS FUNERÁRIOS",
}

categoria_tarifaria_especial = {
    94: "AMBULÂNCIAS",
    95: "AUTO- ESCOLAS",
    96: "BOMBEIROS",
    97: "POLICIAMENTO",
    98: "CASAS VOLANTES, TRAILERS, VEÍCULOS BAR, OFICINAS VOLANTES, VEÍCULOS PAGADO- RES OU PARA TRANSPORTE DE VALORES, HOSPITAIS VOLANTES, VEÍCULOS COM PLATAFORMA ELEVATÓRIA PARA REPAROS EM REDE ELÉTRICA E OUTROS SERVIÇOS, CAMINHÃO ESPARGIDOR DE ASFALTO, VARREDORA MECÂNICA E DESENTUPIDOR DE ESGOTOS E CANOS, VEÍCULOS PARA EXPOSIÇÃO DE PRODUTOS OU FINS PUBLICITÁRIOS",
    99: "CHAPA DE FABRICANTE",
}

text_categoria_tarifaria = """
╒═════════════════════════════════════════════════════════════════════════════════════════════╤════════════╤═════════════╕
│ Categoria                                                                                   │   Nacional │   Importado │
╞═════════════════════════════════════════════════════════════════════════════════════════════╪════════════╪═════════════╡
│ PASSEIO                                                                                     │         10 │          11 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ PICK- UP’S LEVES                                                                            │         14 │          15 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ ESPORTIVOS                                                                                  │         16 │          17 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ MODELOS ESPECIAIS (PASSEIO)                                                                 │         18 │          19 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ PICK- UP’S PESADAS - CARGA: FORD: F100, F1000 e RANGER                                      │         20 │          21 │
│ (Cabine Simples ou Supercab) GM: ACD/10 e 20, SILVERADO e S10 (Cabine Simples ou Estendida) │            │             │
│ TOYOTA PICK- UP E DODGE DAKOTA (Cabine Simples)                                             │            │             │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ PICK- UP’S PESADAS - PESSOAS: FORD: F100, F1000, F250 e RANGER (Cabine Dupla)               │         22 │          23 │
│ GM: ACD/10 e 20, S10 e SILVERADO (Cabine Dupla), BONANZA, S10 BLAZER e VERANEIO.            │            │             │
│ TOYOTA JEEP e GURGEL CARAJÁS DODGE DAKOTA CLUB CAB (Cabine Estendida)                       │            │             │
│ DERIVADAS DE PICK- UP PESADAS FORD e GM                                                     │            │             │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ BICICLETAS MOTORIZADAS, MOTOCICLETAS, MOTONETAS COM REBOQUE OU “SIDE- CAR”,                 │         30 │          31 │
│ VEÍCULOS “ROMI- ISETTA” e VESPACAR.                                                         │            │             │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ CAMINHÕES LEVES (PBT até 10 toneladas)                                                      │         40 │          41 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ CAMINHÕES PESADOS (PBT* acima de 10 toneladas, inclusive)                                   │         42 │          43 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ REBOCADORES                                                                                 │         50 │          51 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ REBOQUES E SEMI- REBOQUES                                                                   │         52 │          53 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ ÔNIBUS E MICROÔNIBUS COM COBRANÇA DE FRETE (exceto urbano com linha regular)                │         58 │          59 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ ÔNIBUS, MICROÔNIBUS COM COBRANÇA DE FRETE (urbano com linha regular)                        │         60 │          61 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ ÔNIBUS, MICROÔNIBUS SEM COBRANÇA DE FRETE                                                   │         62 │          63 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ TRATORES E MÁQUINAS DE USO URBANO                                                           │         68 │          69 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ TRATORES E MÁQUINAS DE USO RURAL                                                            │         70 │          71 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ GUINCHOS (carro socorro)                                                                    │         72 │          73 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ TÁXI                                                                                        │         80 │          81 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ LOTAÇÃO                                                                                     │         82 │          83 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ VEÍCULO ESCOLAR (transporte escolar)                                                        │         84 │          85 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ VIAGEM DE ENTREGA DENTRO DO TERRITÓRIO NACIONAL                                             │         88 │          88 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ VIAGEM DE ENTREGA EXCLUSIVAMENTE PARA PAÍSES DA AMÉRICA DO SUL                              │         89 │          89 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ LOCADORAS                                                                                   │         90 │          91 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ VEÍCULOS FUNERÁRIOS                                                                         │         92 │          93 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ AMBULÂNCIAS                                                                                 │         94 │          94 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ AUTO- ESCOLAS                                                                               │         95 │          95 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ BOMBEIROS                                                                                   │         96 │          96 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ POLICIAMENTO                                                                                │         97 │          97 │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ CASAS VOLANTES, TRAILERS, VEÍCULOS BAR, OFICINAS VOLANTES, VEÍCULOS PAGADO- RES             │         98 │          98 │
│ OU PARA TRANSPORTE DE VALORES, HOSPITAIS VOLANTES, VEÍCULOS COM PLATAFORMA                  │            │             │
│ ELEVATÓRIA PARA REPAROS EM REDE ELÉTRICA E OUTROS SERVIÇOS, CAMINHÃO ESPARGIDOR DE ASFALTO, │            │             │
│ VARREDORA MECÂNICAE DESENTUPIDOR DE ESGOTOS E CANOS, VEÍCULOS PARA EXPOSIÇÃO DE PRODUTOS    │            │             │
│ OU FINS PUBLICITÁRIOS                                                                       │            │             │
├─────────────────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────┤
│ CHAPA DE FABRICANTE                                                                         │         99 │          99 │
╘═════════════════════════════════════════════════════════════════════════════════════════════╧════════════╧═════════════╛"""


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


def solicitar_guinho():
    print("Opção escolhida: Solicitar Guincho")
    while True:
        try:
            cod_tarifa = input(
                "Digite a categoria tarifária (digite 'listar' para ver as categorias e 'cancelar' para cancelar a solicitação): "
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


def settings():
    for key, value in config.items():
        print(f"{key}: {value}")
    resposta = ""
    while resposta != "n":
        resposta = input("\nDesaja alterar alguma configuração? (s/n): ").lower()
        if resposta == "n":
            break
        elif resposta == "s":
            opcao = input("Digite a configuração desejada a ser modificada: ")
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
            solicitar_guinho()
        case 2:
            resumo_operacoes.append("Listar Guinchos")
            listar_guinchos()
        case 3:
            resumo_operacoes.append("Contato")
            contato()
        case 4:
            resumo_operacoes.append("Configurações")
            settings()
        case _:
            print("Opção inexistente")
