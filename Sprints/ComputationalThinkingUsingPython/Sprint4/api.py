import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from cx_Oracle import makedsn
from sqlalchemy.orm import validates

SELF_SIGN_CERT = True

app = Flask(__name__)
api = Api(app)

db_user = "rm98078"
db_pw = "261202"
db_host = "oracle.fiap.com.br"
db_service = "orcl"

oracle_connection_string = "oracle+cx_oracle://{username}:{password}@" + makedsn(
    "{hostname}", "{port}", service_name="{service_name}"
)

app.config["SQLALCHEMY_DATABASE_URI"] = oracle_connection_string.format(
    username=db_user,
    password=db_pw,
    hostname=db_host.split(":")[0],
    port="1521",
    service_name=db_service,
)

# pip install cx-Oracle
# app.config["SQLALCHEMY_DATABASE_URI"] = oracle+cx_oracle://username:password@host:port/dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
if SELF_SIGN_CERT:
    talisman = Talisman(app, content_security_policy=None, force_https=True)


class Modelos(db.Model):
    __tablename__ = "modelos"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    @validates("marca")
    def convert_upper(self, key, value):
        return value.upper()

    @validates("tipo")
    def convert_capitalize(self, key, value):
        return value.capitalize()

    def __init__(self, id, nome, marca, tipo):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.tipo = tipo

    def __repr__(self):
        return "<Modelos %r>" % self.id


app.app_context().push()
db.create_all()


class Main(Resource):
    def get(self, id_modelo=None):
        if id_modelo:
            if not id_modelo.isdigit():
                return {"message": "Invalid ID"}, 400

            modelo = db.session.get(Modelos, id_modelo)
            if modelo:
                return {
                    "id": modelo.id,
                    "nome": modelo.nome,
                    "marca": modelo.marca,
                    "tipo": modelo.tipo,
                }
            else:
                return {"message": "Modelo não encontrado"}, 404
        modelos = Modelos.query.all()
        lista = []
        for modelo in modelos:
            lista.append(
                {
                    "id": modelo.id,
                    "nome": modelo.nome,
                    "marca": modelo.marca,
                    "tipo": modelo.tipo,
                }
            )
        return jsonify(lista)

    def post(self):
        data = request.get_json()
        if "nome" in data and "marca" in data and "tipo" in data:
            if "id" in data:
                modelo = Modelos(data["id"], data["nome"], data["marca"], data["tipo"])
                db.session.add(modelo)
                db.session.commit()
                return {"message": "Modelo cadastrado com sucesso"}, 201
            else:
                lastId = db.session.query(db.func.max(Modelos.id)).scalar()
                modelo = Modelos(lastId + 1, data["nome"], data["marca"], data["tipo"])
                db.session.add(modelo)
                db.session.commit()
                return {
                    "message": f"Modelo cadastrado com sucesso com id {lastId}"
                }, 201
        else:
            return {"message": "Erro ao cadastrar modelo"}, 400

    def put(self, id_modelo):
        data = request.get_json()
        modelo = Modelos.query.get(id_modelo)
        if modelo:
            if "nome" in data:
                modelo.nome = data["nome"]
            if "marca" in data:
                modelo.marca = data["marca"]
            if "tipo" in data:
                modelo.tipo = data["tipo"]
            db.session.commit()
            return {"message": "Modelo atualizado com sucesso"}, 200
        else:
            return {"message": "Modelo não encontrado"}, 404

    def delete(self, id_modelo):
        modelo = Modelos.query.get(id_modelo)
        if modelo:
            db.session.delete(modelo)
            db.session.commit()
            return {"message": "Modelo deletado com sucesso"}, 200
        else:
            return {"message": "Modelo não encontrado"}, 404


api.add_resource(Main, "/", "/<id_modelo>")

if __name__ == "__main__":
    # Checa se a tabela de modelos está vazia, se estiver, preenche com os dados do arquivo modelos.json
    if not db.session.query(Modelos.id).count():
        with open("./data/modelos.json") as f:
            data = json.load(f)
            for modelo in data:
                modelo = Modelos(
                    id=modelo["ID"],
                    nome=modelo["NOME"],
                    marca=modelo["MARCA"],
                    tipo=modelo["TIPO"],
                )
                db.session.add(modelo)
        db.session.commit()
    if SELF_SIGN_CERT:
        app.run(port=8080, debug=True, ssl_context=("cert.pem", "key.pem"))
    else:
        app.run(port=8080, debug=True)


# ENDPOINTS:
# GET / - retorna todos os modelos
# GET /<id> - retorna um modelo
# POST / - cria um novo modelo
# PUT /<id> - atualiza um modelo
# DELETE /<id> - remove um modelo
