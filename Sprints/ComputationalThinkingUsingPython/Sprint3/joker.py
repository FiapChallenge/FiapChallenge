# Correção dos IDS pois a database tinha veíuculos aquáticos que não foram inseridos

import json

with open('data/modelos.json', mode='r+', encoding='utf-8') as f:
    data = json.load(f)
    
    print(len(data))
    print(data[0]["ID"])
    print(data[-1]["ID"])
    
    for i, modelo in enumerate(data):
        modelo["ID"] = i
        
    for modelo in data:
        print(modelo)
    
    f.seek(0)
    json.dump(data, f, indent=4, ensure_ascii=False)