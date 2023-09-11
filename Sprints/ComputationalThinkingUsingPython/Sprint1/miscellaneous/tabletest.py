from tabulate import tabulate

categoria_tarifaria = [
    ["PASSEIO", 10, 11],
    ["PICK- UP’S LEVES", 14, 15],
    ["ESPORTIVOS", 16, 17],
    ["MODELOS ESPECIAIS (PASSEIO)", 18, 19],
    [
        "PICK- UP’S PESADAS - CARGA: FORD: F100, F1000 e RANGER\n(Cabine Simples ou Supercab) GM: ACD/10 e 20, SILVERADO e S10 (Cabine Simples ou Estendida)\nTOYOTA PICK- UP E DODGE DAKOTA (Cabine Simples)",
        20,
        21,
    ],
    [
        "PICK- UP’S PESADAS - PESSOAS: FORD: F100, F1000, F250 e RANGER (Cabine Dupla)\nGM: ACD/10 e 20, S10 e SILVERADO (Cabine Dupla), BONANZA, S10 BLAZER e VERANEIO.\nTOYOTA JEEP e GURGEL CARAJÁS DODGE DAKOTA CLUB CAB (Cabine Estendida)\nDERIVADAS DE PICK- UP PESADAS FORD e GM",
        22,
        23,
    ],
    [
        "BICICLETAS MOTORIZADAS, MOTOCICLETAS, MOTONETAS COM REBOQUE OU “SIDE- CAR”,\nVEÍCULOS “ROMI- ISETTA” e VESPACAR.",
        30,
        31,
    ],
    ["CAMINHÕES LEVES (PBT até 10 toneladas)", 40, 41],
    ["CAMINHÕES PESADOS (PBT* acima de 10 toneladas, inclusive)", 42, 43],
    ["REBOCADORES", 50, 51],
    ["REBOQUES E SEMI- REBOQUES", 52, 53],
    [
        "ÔNIBUS E MICROÔNIBUS COM COBRANÇA DE FRETE (exceto urbano com linha regular)",
        58,
        59,
    ],
    ["ÔNIBUS, MICROÔNIBUS COM COBRANÇA DE FRETE (urbano com linha regular)", 60, 61],
    ["ÔNIBUS, MICROÔNIBUS SEM COBRANÇA DE FRETE", 62, 63],
    ["TRATORES E MÁQUINAS DE USO URBANO", 68, 69],
    ["TRATORES E MÁQUINAS DE USO RURAL", 70, 71],
    ["GUINCHOS (carro socorro)", 72, 73],
    ["TÁXI", 80, 81],
    ["LOTAÇÃO", 82, 83],
    ["VEÍCULO ESCOLAR (transporte escolar)", 84, 85],
    ["VIAGEM DE ENTREGA DENTRO DO TERRITÓRIO NACIONAL", 88, 88],
    ["VIAGEM DE ENTREGA EXCLUSIVAMENTE PARA PAÍSES DA AMÉRICA DO SUL", 89, 89],
    ["LOCADORAS", 90, 91],
    ["VEÍCULOS FUNERÁRIOS", 92, 93],
    ["AMBULÂNCIAS", 94, 94],
    ["AUTO- ESCOLAS", 95, 95],
    ["BOMBEIROS", 96, 96],
    ["POLICIAMENTO", 97, 97],
    [
        "CASAS VOLANTES, TRAILERS, VEÍCULOS BAR, OFICINAS VOLANTES, VEÍCULOS PAGADO- RES\nOU PARA TRANSPORTE DE VALORES, HOSPITAIS VOLANTES, VEÍCULOS COM PLATAFORMA\nELEVATÓRIA PARA REPAROS EM REDE ELÉTRICA E OUTROS SERVIÇOS, CAMINHÃO ESPARGIDOR DE ASFALTO,\nVARREDORA MECÂNICAE DESENTUPIDOR DE ESGOTOS E CANOS, VEÍCULOS PARA EXPOSIÇÃO DE PRODUTOS\nOU FINS PUBLICITÁRIOS",
        98,
        98,
    ],
    ["CHAPA DE FABRICANTE", 99, 99],
]

print(
    tabulate(
        categoria_tarifaria,
        headers=["Categoria", "Nacional", "Importado"],
        tablefmt="fancy_grid",
    )
)
