from database import db

class Orcamento(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    largura = db.Column(db.Float)

    altura = db.Column(db.Float)

    profundidade = db.Column(db.Float)

    preco_mdf = db.Column(db.Float)

    preco_final = db.Column(db.Float)

    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))

    def to_dict(self):

        return {
            "id": self.id,
            "largura": self.largura,
            "altura": self.altura,
            "profundidade": self.profundidade,
            "preco_mdf": self.preco_mdf,
            "preco_final": self.preco_final,
            "cliente_id": self.cliente_id
        }