from flask import Blueprint, request, render_template, redirect
from database import db
from models.cliente import Cliente

clientes_bp = Blueprint("clientes", __name__)


@clientes_bp.route("/clientes_page")
def pagina_clientes():

    clientes = Cliente.query.all()

    return render_template(
        "clientes.html",
        clientes=clientes
    )


@clientes_bp.route("/clientes", methods=["POST"])
def criar_cliente():

    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form["email"]

    novo_cliente = Cliente(
        nome=nome,
        telefone=telefone,
        email=email
    )

    db.session.add(novo_cliente)
    db.session.commit()

    return redirect("/clientes_page")


@clientes_bp.route("/clientes/editar/<int:id>", methods=["POST"])
def editar_cliente(id):

    cliente = Cliente.query.get(id)

    cliente.nome = request.form["nome"]
    cliente.telefone = request.form["telefone"]
    cliente.email = request.form["email"]

    db.session.commit()

    return redirect("/clientes_page")


@clientes_bp.route("/clientes/deletar/<int:id>")
def deletar_cliente(id):

    cliente = Cliente.query.get(id)

    db.session.delete(cliente)
    db.session.commit()

    return redirect("/clientes_page")