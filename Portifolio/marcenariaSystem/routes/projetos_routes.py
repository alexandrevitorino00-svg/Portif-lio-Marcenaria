from flask import Blueprint, request, render_template, redirect
from database import db
from models.projeto import Projeto
from models.cliente import Cliente

projetos_bp = Blueprint("projetos", __name__)

@projetos_bp.route("/projetos_page")
def pagina_projetos():

    clientes = Cliente.query.all()
    projetos = Projeto.query.all()

    return render_template(
        "projetos.html",
        clientes=clientes,
        projetos=projetos
    )

@projetos_bp.route("/projeto", methods=["POST"])
def criar_projeto():

    nome = request.form["nome"]
    cliente_id = int(request.form["cliente_id"])
    status = request.form["status"]

    novo_projeto = Projeto(
        nome=nome,
        cliente_id=cliente_id,
        status=status
    )

    db.session.add(novo_projeto)
    db.session.commit()

    return redirect("/projetos_page")


@projetos_bp.route("/projeto/editar/<int:id>", methods=["POST"])
def editar_projeto(id):

    projeto = Projeto.query.get(id)

    projeto.nome = request.form["nome"]
    projeto.cliente_id = int(request.form["cliente_id"])
    projeto.status = request.form["status"]

    db.session.commit()

    return redirect("/projetos_page")


@projetos_bp.route("/projeto/deletar/<int:id>")
def deletar_projeto(id):

    projeto = Projeto.query.get(id)

    db.session.delete(projeto)
    db.session.commit()

    return redirect("/projetos_page")