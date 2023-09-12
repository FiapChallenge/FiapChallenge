# pegue apenas os json com tipo caminhão e transforme em csv

import json
import csv

with open('./data/modelos.json', "r+", encoding="utf-8-sig") as f:
    data = json.load(f)
    with open('./data/caminhoes.csv', 'r+', newline='', encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['NOME', 'MARCA'])
        for i in range(len(data)):
            if data[i]['TIPO'] == 'Caminhão':
                writer = csv.writer(file, delimiter=';')
                writer.writerow([data[i]['NOME'], data[i]['MARCA']])
                
                