from flask import Blueprint, request, render_template, redirect
from database import db
from models.orcamento import Orcamento
from models.cliente import Cliente
from services.calculo_orcamento import calcular_orcamento
from services.pdf_service import gerar_pdf

orcamentos_bp = Blueprint("orcamentos", __name__)


@orcamentos_bp.route("/orcamentos_page")
def pagina_orcamentos():

    clientes = Cliente.query.all()

    return render_template(
        "orcamento.html",
        clientes=clientes,
        preco_final=None
    )


@orcamentos_bp.route("/orcamento", methods=["POST"])
def criar_orcamento():

    largura = float(request.form["largura"])
    altura = float(request.form["altura"])
    profundidade = float(request.form["profundidade"])
    preco_mdf = float(request.form["preco_mdf"])
    cliente_id = int(request.form["cliente_id"])

    resultado = calcular_orcamento(
        largura,
        altura,
        profundidade,
        preco_mdf
    )

    novo_orcamento = Orcamento(
        largura=largura,
        altura=altura,
        profundidade=profundidade,
        preco_mdf=preco_mdf,
        preco_final=resultado["preco_final"],
        cliente_id=cliente_id
    )

    db.session.add(novo_orcamento)
    db.session.commit()

    clientes = Cliente.query.all()

    return render_template(
        "orcamento.html",
        clientes=clientes,
        preco_final=resultado["preco_final"]
    )


@orcamentos_bp.route("/orcamento/pdf/<int:id>")
def gerar_pdf_orcamento(id):

    orcamento = Orcamento.query.get_or_404(id)

    caminho_pdf = gerar_pdf(orcamento)

    return {
        "mensagem": "PDF gerado",
        "arquivo": caminho_pdf
    }