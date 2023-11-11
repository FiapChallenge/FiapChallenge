from api import db, Modelos


class ModelosCRUD:
    @staticmethod
    def type_of_sort(sort_by):
        if sort_by == "ID":
            return Modelos.id
        if sort_by == "NOME":
            return Modelos.nome
        if sort_by == "MARCA":
            return Modelos.marca
        if sort_by == "TIPO":
            return Modelos.tipo
        return Modelos.id

    @staticmethod
    def get_all_modelos(sort_by="ID"):
        modelos = Modelos.query.order_by(ModelosCRUD.type_of_sort(sort_by)).all()
        lista = []
        for modelo in modelos:
            lista.append(
                {
                    "ID": modelo.id,
                    "NOME": modelo.nome,
                    "MARCA": modelo.marca,
                    "TIPO": modelo.tipo,
                }
            )
        return lista

    @staticmethod
    def get_modelo_by_id(modelo_id):
        modelo = Modelos.query.order_by().get(modelo_id)
        if modelo:
            return {
                "ID": modelo.id,
                "NOME": modelo.nome,
                "MARCA": modelo.marca,
                "TIPO": modelo.tipo,
            }
        else:
            return None

    @staticmethod
    def get_modelos_by_tipo(modelo_tipo, sort_by="ID"):
        modelos = (
            Modelos.query.order_by(ModelosCRUD.type_of_sort(sort_by))
            .filter_by(tipo=modelo_tipo)
            .all()
        )
        lista = []
        for modelo in modelos:
            lista.append(
                {
                    "ID": modelo.id,
                    "NOME": modelo.nome,
                    "MARCA": modelo.marca,
                    "TIPO": modelo.tipo,
                }
            )
        return lista

    @staticmethod
    def get_modelos_by_marca(modelo_marca, sort_by="ID"):
        modelos = (
            Modelos.query.order_by(ModelosCRUD.type_of_sort(sort_by))
            .filter_by(marca=modelo_marca)
            .all()
        )
        lista = []
        for modelo in modelos:
            lista.append(
                {
                    "ID": modelo.id,
                    "NOME": modelo.nome,
                    "MARCA": modelo.marca,
                    "TIPO": modelo.tipo,
                }
            )
        return lista

    @staticmethod
    def get_modelos_by_tipo_marca(modelo_tipo, modelo_marca, sort_by="ID"):
        modelos = (
            Modelos.query.order_by(ModelosCRUD.type_of_sort(sort_by))
            .filter_by(tipo=modelo_tipo)
            .filter_by(marca=modelo_marca)
            .all()
        )
        lista = []
        for modelo in modelos:
            lista.append(
                {
                    "ID": modelo.id,
                    "NOME": modelo.nome,
                    "MARCA": modelo.marca,
                    "TIPO": modelo.tipo,
                }
            )
        return lista

    @staticmethod
    def create_modelo(id, nome, marca, tipo):
        modelo = Modelos(id=id, nome=nome, marca=marca, tipo=tipo)
        db.session.add(modelo)
        db.session.commit()
        return modelo.id

    @staticmethod
    def update_modelo(modelo_id, nome=None, marca=None, tipo=None):
        modelo = Modelos.query.get(modelo_id)
        if modelo:
            if nome is not None:
                modelo.nome = nome
            if marca is not None:
                modelo.marca = marca
            if tipo is not None:
                modelo.tipo = tipo
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def delete_modelo(modelo_id):
        modelo = Modelos.query.get(modelo_id)
        if modelo:
            db.session.delete(modelo)
            db.session.commit()
            return True
        else:
            return False
