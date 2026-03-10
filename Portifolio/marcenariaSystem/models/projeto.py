from database import db

class Projeto(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(120), nullable=False)

    status = db.Column(db.String(50), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))

    cliente = db.relationship("Cliente")